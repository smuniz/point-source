# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc
from traceback import format_exc

from actionplan import Action, ActionPlan, ActionPlanException

from idioms import IdiomAnalyzerException

from misc.prerequisites import require

require("frontend.symbols")
from symbols import SymbolsManager, SymbolsManagerException

##reload(frontend.generic_disasm.base)
#require("frontend.generic_disasm.base")
#from frontend.generic_disasm.base import BaseDebuggerException

#reload(middleend.mir_exception)
require("middleend.mir_exception")
from middleend.mir_exception import MiddleIrException

#reload(middleend.mir.mir_module)
require("middleend.mir.mir_module")
from middleend.mir.mir_module import MiddleIrModule, MiddleIrModuleException

#reload(middleend.mir.mir_basicblock)
require("middleend.mir.mir_basicblock")
from middleend.mir.mir_basicblock import MiddleIrBasicBlock

#reload(middleend.mir.mir_instruction)
require("middleend.mir.mir_instruction")
from middleend.mir.mir_instruction import MiddleIrInstructionBuilder

#reload(middleend.mir.mir_function)
require("middleend.mir.mir_function")
from middleend.mir.mir_function import *

#import middleend.mir.mir_type
#reload(middleend.mir.mir_type)
#require("middleend.mir.mir_type")
from middleend.mir.mir_type import *

__all__ = ["FrontEnd", "FrontEndException"]

#
# Only one instance is required to store all the symbolic information
# pertaining to this binary.
#
symbols_tables = SymbolsManager()


class FrontEndException(Exception):
    """Front-end base exception class."""
    pass


class FrontEnd(object):
    """
    Base class for different Front-Ends to support multiple decompilable
    architectures.

    All the generic operations related to the front-end will be performed by
    the FrontEnd class leaving architecture specific operations to the derived
    class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, idiom_analyzer_type, debugger):
        """Perform base front-end instance initialization."""
        self.action_plan = ActionPlan()

        # Current debugger application
        self.debugger = debugger

        # Storage for all the different types of low level groups of
        # operations for current architecture.
        self.unimplemented_types = debugger.unimplemented_types
        self.conditional_branch_types = debugger.conditional_branch_types
        self.unconditional_branch_types = debugger.unconditional_branch_types
        self.assignment_types = debugger.assignment_types

        self.function_address = None

        # Low-level IR of the current function being decompiled. This is an
        # abstraction from the debugger structures to represent the
        # disassembled code.
        self.lir_function = None

        # Store the MIR function being decompiled.
        self.mir_function = None

        # Create a Middle level intermediate representation of the current
        # module that posses the function being decompiled if it wasn't already
        # created and associate a function IR to it.
        #
        # This will return always the same module in case we specify the same
        # filename on the input file.
        #
        self.mir_module = MiddleIrModule.new(self.debugger.get_input_file())

        # Set the module in charge of idiom analysis.
        self.idiom_analyzer_type = idiom_analyzer_type
        self.idiom_analyzer = None

        # Setup symbol table for local/global variables refrences, etc..
        global symbols_tables
        self.symbols_tables = symbols_tables

        # Development flags
        self.debug_inst_info = True

        # Current architectures instruction set to work with.
        self.iset = self.debugger.instruction_set

        # This dictionary contains all the LIR function analyzed during this
        # run to avoid wasting resources by analyzing the same function twice.
        self.lir_functions_cache = dict()

    @property
    def name(self):
        """Return the formatted name of the current front-end."""
        return "FrontEnd%s" % self.TARGET_ARCH

    @property
    def debugger(self):
        """Return the debugger instance for the current application."""
        return self._debugger

    @debugger.setter
    def debugger(self, debugger):
        """Store the debugger instance for the current application."""
        self._debugger = debugger

    def generate_mir_skeleton(self):
        """
        Create the basic MIR structure (function with its basic blocks) in
        order to facilitate the first phase of the idioms analysis.

        Further analysis should discard idioms and as a result a more compact
        and accurate IR will be obtained to feed the decompiler final phase
        known as the Back-end.

        """
        #
        # Initialize internal MIR members for further usage.
        #
        function_name = self.lir_function.name

        # TODO / FIXME: Correctly detect return type.
        # Create basic return types in order to create the function skeleton.
        # At the moment we just create generic (integer) types with the right
        # amount of return values.
        self.return_type = 1

        if self.return_type == 0:
            return_type = MiddleIrTypeVoid()
        elif self.return_type == 1:
            return_type = MiddleIrTypeInt()
        else:
            raise FrontEndException("Unknown return type (%d)" % \
                self.return_type)

        self.mir_function = MiddleIrFunction.get(self.mir_module, function_name)
        if self.mir_function is not None:
            # Delete the previously created function and create a new one. This
            # is what the user requested so do it (definition might have
            # changed, etc.).
            if self.mir_function in self.symbols_tables:
                del self.symbols_tables[self.mir_function.name]
            self.mir_function.delete()

        # Seems like the function doesn't already exists in our store so
        # we'll create a new one.
        self.mir_function = MiddleIrFunction.new(self.mir_module, function_name, return_type)

        # TODO / FIXME : Determine parameter types.
        #self.mir_function.arguments([MiddleIrTypeInt(), MiddleIrTypeInt()])

        # Set the default calling convention.
        #self.mir_function.set_calling_convention(CALL_CONV_C)

        self.mir_inst_builder = None

        #
        # Iterate through LIR to transfor it into its MIR representation (this
        # is a first pass, so just the basic skeleton will be created and
        # further passes will create the rest).
        #
        for lir_basic_block in self.lir_function:

            # Create the MIR basic block instance and add a label to it
            # using an existing one (if any) or creating a new one.
            mir_basic_block = MiddleIrBasicBlock()

            # Get the name of the local label only if the address doesn't
            # belong to the first instruction (in this case IDA returns
            # the name of the function and we don't want this.).

            if lir_basic_block == self.lir_function[0]:
                label = "entry"  # LLVM convention

            else:
                label = self.debugger.get_address_label(
                    lir_basic_block.start_address)

                if not label:
                    # TODO: Will not work on functions with multiple ending
                    # basic blocks.
                    if lir_basic_block != self.lir_function[-1]:

                        # We try to obtain the name as it's already visible because
                        # the user might have changed it.
                        # It could happen that some locations do not have a local
                        # label because it's via a direct flow that the location is
                        # reached so we create a label name similar to the ones
                        # produced by IDA and use it instead.
                        #label = "loc_%X" % lir_basic_block.start_address
                        label = "loc_%X" % lir_basic_block[0].address

                    else:
                        label = "return"
                        #label = "ret_loc_%X" % lir_basic_block.start_address

            #
            # Setup additional basic block information and finally store the
            # filled block in the current function instance.
            #
            self.mir_function.add_basic_block(mir_basic_block)

            mir_basic_block.label = label

            mir_basic_block.instruction_builder = \
                MiddleIrInstructionBuilder(mir_basic_block)

            # TODO/FIXME: This is a horrible kludge!
            #
            # We set this here because the phase 1 idiom analysis need to know
            # basic block boundaries in order to obtain the instruction builder
            # for specific instruction addresses.
            #
            # Normally the basic block boundaries should be set according to
            # its instruction addresses.
            mir_basic_block.start_address = lir_basic_block.start_address
            mir_basic_block.end_address = lir_basic_block.end_address

    def populate_mir(self):
        """Convert all the function's instructions represented by the LIR to a
        higher IR called MIR (Middle-end Intermediate Representation) as an
        initial step.

        """
        # Propagate addresses by adding each prologue and epilogue address to
        # the list of addresses in the MIR function in order to keep track of
        # assembly->MIR addrresses during translation.
        print "[+] Propagatin LIR-to-MIR prologue and epilogue addresses."

        for address in self.lir_function.prologue_addresses:
            self.mir_function.add_prologue_address(address)

        self.mir_function.add_address(self.lir_function.start_address)

        for address in self.lir_function.epilogue_addresses:
            self.mir_function.add_epilogue_address(address)

        self.mir_function.add_address(self.lir_function.start_address)

        #
        # Initiate instruction translation phase.
        #
        for lir_basic_block_index, lir_basic_block in enumerate(self.lir_function):

            address = lir_basic_block.start_address

            self.mir_inst_builder = \
                self.mir_function.get_instruction_builder_by_address(
                    address, False)

            mir_basic_block = self.mir_function[lir_basic_block_index]

            for lir_inst in lir_basic_block:

                # Avoid already detected instructions in idioms and other
                # analysis.
                if lir_inst.analyzed:
                    #print "---> inst at 0x%X was already analyzed..." \
                    #    "skipping" % lir_inst.address
                    continue

                #
                # This step is very important. This is where most of the LIR 
                # instruction are translated to its MIR equivalents for
                # further usage.
                #
                try:
                    mir_inst = self.transform_to_mir_instruction(lir_inst)
                except FrontEndException, err:
                    print format_exc()
                    raise FrontEndException(
                        "Unable to transform LIR instruction (%s) : %s" % \
                        (lir_inst, err))

                if mir_inst is not None:

                    # Set MIR instruction address equal to the LIR instruction
                    # used to get it,
                    # Store the instruction address for debugging purposes.
                    # Some LLVM IR code are not instructions but declarations
                    # or other stuff that doesn't support add_address method.
                    mir_inst.add_address(lir_inst.address)

                    # Now the newly created instruction is stored in a basic
                    # block, whose purpose is to represent a group of
                    # instructions altogether.
                    mir_basic_block.add_instruction(mir_inst)

                    self.__display_instruction_information(
                        lir_inst, lir_inst.group_name)

                    # Copy all graph information from low-level representation to the
                    # intermediate-level language.
                    #self.__propagate_graph_information()

    def transform_to_mir_instruction(self, lir_inst):
        """Get the corresponding MIR instruction according to the LIR
        instruction.

        This is architecture-specific so the opcodes are grouped by type and
        this is done inside the front-end of every architecture.

        """
        #
        # First we check if the instruction at the current address was
        # previously analyzed and marked for convertion by the idiom analyzer.
        #
        if self.action_plan.has_plan_for_address(lir_inst.address):
            pass

        #
        # Dispatch the current LIR instruction to be appropriate type
        # convertion routine to be transformed into its equivalent MIR
        # instruction(s).
        #
        mir_inst = None
        group = lir_inst.group_name

        try:
            if lir_inst.type in self.assignment_types:
                mir_inst = self.on_assignment(lir_inst)

            elif lir_inst.type in self.unconditional_branch_types:
                mir_inst = self.on_unconditional_branch(lir_inst)

            elif lir_inst.type in self.conditional_branch_types:
                mir_inst = self.on_conditional_branch(lir_inst)

            elif lir_inst.type in self.unimplemented_types:
                mir_inst = self.on_unknown(lir_inst)

            else:
                #mir_inst = self.on_unknown(lir_inst)
                raise FrontEndException(
                    "Unsupported instruction at 0x%X on '%s' group." % \
                        (lir_inst.address, group))

        except FrontEndException, err:
            raise FrontEndException(err)

        return mir_inst

    def __propagate_graph_information(self):
        """
        With all the function instructions and basic blocks created, the
        information from the basic blocks referencing each other is set (this
        is used for the function graph analysis and others).

        """
        for bb_index, lir_bb in enumerate(self.lir_function):

            for edge_ea in self.lir_function[bb_index].get_in_edges():
                bblock = self.lir_function.get_basic_block_by_address(edge_ea)
                bblock_index = self.lir_function.get_basic_block_index(bblock)

                block = self.mir_function[bblock_index]

                self.mir_function[bb_index].add_in_edge(bblock_index)

    @property
    def function_address(self):
        """Return the address of the function being decompiled."""
        return self._function_address

    @function_address.setter
    def function_address(self, address):
        """Store the address of the function being decompiled."""
        self._function_address = address

    def __dump_lir(self):
        """Dump the current LIR function to the debugger output."""
        print "[+] LIR representation:\n%s" % self.lir_function

    def analyze(self):
        """Start the analysis phase by gathering information about all the
        instructions contained inside the function being analyzed and also
        store information about call graph for further operations.

        """
        try:
            print "[+] Generating Low level IR..."
            self.lir_function = self.debugger.generate_lir(self.function_address)

            print "[+] Found %d basic block(s) on function \'%s\' containing %d " \
                "instruction(s)" % (
                self.lir_function.get_basic_blocks_count(),
                self.lir_function.name,
                self.lir_function.instructions_count)

            # Output LIR for debugging purposes.
            #self.__dump_lir()
        except Exception, err:
            raise FrontEndException(
                "Unable to generate Low Level IR: %s" % err)

        try:
            #
            # Step x
            #
            # Initialize internal MIR members for further usage.
            #
            print "[+] Creating Middle level IR skeleton..."
            self.generate_mir_skeleton()

            self.perform_live_variable_analysis(self.lir_function, 1)

            print "[+] Total functions analyzed : %d" % len(self.lir_functions_cache)

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            #
            self.current_symbols_table = \
                self.symbols_tables.symbols(self.lir_function.start_address)

            print "[+] Initializing idioms analyser..."
            if self.idiom_analyzer is None:
                self.idiom_analyzer = self.idiom_analyzer_type(self.debugger)

            # Clean any internal state from previous analysis.
            self.idiom_analyzer.init(
                self.lir_function, self.mir_function, self.symbols_tables)

            print "[+] Initiating idioms analysis phase 1..."
            self.idiom_analyzer.perform_phase1_analysis()

            self.__dump_lir()
            #
            # Step x
            #
            # With the middle level IR created proceed to the idioms analysis
            # using the newly created IR and filling it with all the
            # appropriate code representation.
            #
            print "[+] Populating Middle level IR..."
            self.populate_mir()

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            #
            print "[+] Initiating idioms analysis phase 2..."
            self.idiom_analyzer.perform_phase2_analysis()

        except IdiomAnalyzerException, err:
            #print format_exc() + '\n'
            raise FrontEndException("Idioms analysis failed (%s)" % err)

        except MiddleIrException, err:
            #print format_exc() + '\n'
            raise FrontEndException("Middle IR error (%s)" % err)

        #
        # Step x
        #
        # Perform a series of verifications in the MIR to make sure all the
        # operations were correctly (this is done internally by LLVM).
        #
        print "[+] Verifying Middle level IR code..."
        self.mir_module.verify()

    def perform_live_variable_analysis(self, lir_function, depth=None):
        """Perform live analysis on variables based on their usage in called
        functions.

        """
        # Iterate through every instruction present in the function in order to
        # get information about the parameters usage and return values of the
        # called functions.
        for lir_basic_block in lir_function:
            for lir_inst in lir_basic_block:

                callee_address = self._extract_callee_address(lir_inst)
                
                if callee_address is None:
                    # In case that the call instruction didn't use a guessable
                    # address we just move on.
                    continue

                if callee_address in self.lir_functions_cache:
                    continue

                # Analyze the called function in order to obtain parameters and
                # return registers information.
                print "[+] Analyzing callee at 0x%X" % callee_address
                lir_callee = self.analyze_callee(callee_address)

                if lir_callee:

                    print "    - Found %d basic block(s) on function \'%s\' containing %d " \
                        "instruction(s)" % (
                        lir_callee.get_basic_blocks_count(),
                        lir_callee.name,
                        lir_callee.instructions_count)

                    self.lir_functions_cache.setdefault(callee_address, lir_callee)

                    # Recurse into callees until we reach the specified level
                    # (in case it was specified).
                    if depth is None:
                        continue
                    if depth > 0:
                        depth -= 1
                    else:
                        continue

                    # Analyse the calle function and its callees (if
                    # appropriate according to the depth level).
                    self.perform_live_variable_analysis(lir_callee, depth)

    @abc.abstractmethod
    def analyze_callee(self, callee_address):
        """Analyze the callee function by performing a live analysis on it."""
        return

    @abc.abstractmethod
    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        return

    @abc.abstractmethod
    def is_call_instruction(self, lir_inst):
        """Determine if the specified instruction is a call instruction or
        not.

        """
        return

    @property
    def mir(self):
        """Return the intermediate level presentation ofthe current function
        being decompiled.
        
        """
        return self.mir_module

    @mir.setter
    def mir(self, mir_module):
        """Store the intermediate level presentation ofthe current function
        being decompiled.
        
        """
        self.mir_module = mir_module

    def __display_instruction_information(self, lir_inst, lir_group):
        """Print information about the assembler instruction specified which
        belong to the group parameter.

        """
        if self.debug_inst_info:

            address = lir_inst.address
            arch = self.TARGET_ARCH
            group = lir_group.capitalize()
            inst_repr = str(lir_inst)
            inst_numb = lir_inst.type

            print "\t0x%(address)08X - %(arch)s %(group)15s " \
                  "(type %(inst_numb)3d) - %(inst_repr)-25s" % vars()
