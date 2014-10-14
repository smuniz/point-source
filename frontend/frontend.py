# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import format_exc

from actionplan import Action, ActionPlan, ActionPlanException

from idioms import IdiomAnalyzerException

from misc.prerequisites import require

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
# Store the symbol tables that belong to each and every function being
# analyzed.
#
symbol_tables = dict()

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

    def __init__(self, idiom_analyzer, debugger):
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
        self.mir_module = MiddleIrModule(self.debugger.get_input_file())

        # Set the module in charge of idiom analysis.
        self.idiom_analyzer = idiom_analyzer
                
        # Setup symbol table for local/global variables refrences, etc..
        global symbol_tables
        self.symbol_tables = symbol_tables

        # Development flags
        self.debug_inst_info = True

        # Current architectures instruction set to work with.
        self.iset = self.debugger.instruction_set

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
        function_name = self.debugger.get_current_function_name()

        #self.mir_function = self.mir_module.create_function(function_name)
        # TODO / FIXME : Should add address boundaries.
        self.mir_function = MiddleIrFunction(function_name)

        # Create basic return types in order to create the function skeleton.
        # At the moment we just create generic (integer) types with the right
        # amount of return values.
        # TODO / FIXME: Fix this horrible kludge!!!
        self.return_type = 1

        if self.return_type == 0:
            # Do nothing because the function was initialized with 'void' type.
            pass
        elif self.return_type == 1:
            ret_type = MiddleIrTypeInt()
        else:
            raise FrontEndException("Unknown return type (%d)" % \
                self.return_type)

        self.mir_function.return_type = ret_type

        # TODO / FIXME : Determine parameter types.
        #self.mir_function.parameters([MiddleIrTypeInt(), MiddleIrTypeInt()])

        self.mir_module.add_function(self.mir_function)
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

    def generate_mir(self):
        """Convert all the function's instructions represented by the LIR to a
        higher IR called MIR (Middle-end Intermediate Representation) as an
        initial step.

        """

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
                except Exception, err:
                    # TODO : Replace this exception handler with a front-end
                    # one.
                    print format_exc()
                    raise FrontEndException(
                        "Unable to transform LIR instruction (%s) : %s" % \
                        (lir_inst, err))

                if mir_inst is not None:
                    # Now the newly created instruction is stored in a basic
                    # block, whose purpose is to represent a group of
                    # instructions altogether.
                    mir_basic_block.add_instruction(mir_inst)

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

        if mir_inst is not None:
            # Set MIR instruction address equal to the LIR instruction used
            # to get it.
            # Store the instruction address for debugging purposes.
            # Some LLVM IR code are not instructions but declarations or other
            # stuff that doesn't support add_address method.
            mir_inst.add_address(lir_inst.address)
        #else:
        #    raise FrontEndException(
        #        "Empty instruction at 0x%X on '%s' group." % \
        #            (lir_inst.address, group))

        self.__display_instruction_information(lir_inst, group)

        #if not mir_inst:
        #    mir_inst = self.on_unknown(lir_inst)

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

    def generate_lir(self):
        """
        Based on the low level instruction previously obtained by the
        disassembler layer, proceed to create a LIR representation of the
        current function under analysis.

        This is specific to the disassembler engine where the decompiler is run
        into.
        """
        #
        # Get every instruction with it's operands and basic blocks
        # information and generate the Low level IR (aka LIR).
        #
        self.lir_function = self.debugger.generate_lir(
            self.function_address)

        #
        # Perform a basic check on newly generated LIR function.
        #
        if self.lir_function.get_basic_blocks_count() == 0:
            raise FrontEndException(
                "No basic blocks found during the analysis.")

        if self.lir_function.instructions_count == 0:
            raise FrontEndException(
                "No instructions found during the analysis.")

        print "[+] Generating DU and UD chains for Low level IR..."
        self.lir_function.generate_chains()

        print "[+] Found %d basic block(s) on function \'%s\' containing %d " \
            "instruction(s)" % (
            self.lir_function.get_basic_blocks_count(),
            self.lir_function.name,
            self.lir_function.instructions_count)

    def analyze(self):
        """Start the analysis phase by gathering information about all the
        instructions contained inside the function being analyzed and also
        store information about call graph for further operations.

        """
        print "[+] Generating Low level IR..."
        self.generate_lir()

        # Output LIR for debugging purposes.
        #self.__dump_lir()

        try:
            #
            # Step x
            #
            # Initialize internal MIR members for further usage.
            #
            print "[+] Creating Middle level IR skeleton..."
            self.generate_mir_skeleton()

            #
            # Step x
            #
            # Invoke the appropriate idiom analyzer for the current architecture.
            #
            self.current_symbol_table = self.symbol_tables.setdefault(self.mir_function, dict())

            print "[+] Initializing idioms analyser..."
            self.idiom_analyzer = self.idiom_analyzer(
                self.debugger,
                self.lir_function,
                self.mir_module,
                self.mir_function,
                self.symbol_tables)

            print "[+] Initiating idioms analysis phase 1..."
            self.idiom_analyzer.perform_phase1_analysis()

            self.__dump_lir()
            #
            # Step x
            #
            # Create the middle level IR and then proceed to the idioms analysis
            # using the newly created IR.
            #
            print "[+] Creating Middle level IR..."
            self.generate_mir()

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

        #
        # Step x
        #
        # Perform a series of verifications in the MIR to make sure all the
        # operations were correctly (this is done internally by LLVM).
        #
        print "[+] Verifying Middle level IR code..."
        self.mir_module.verify()

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
