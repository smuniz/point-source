# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc
from traceback import format_exc
from copy import copy

__all__ = ["BaseDebugger",
           "BaseDebuggerException",
           "PPC_ARCH",
           "MIPS_ARCH",
           "ARM_ARCH",
           "AARCH64_ARCH",
           "X86_ARCH",
           "X86_64_ARCH"]

PPC_ARCH = 0
MIPS_ARCH = 1
ARM_ARCH = 2
AARCH64_ARCH = 3
X86_ARCH = 4
X86_64_ARCH = 5

#
# Keep track of every LIR function represented in LIR form so when one is
# requested a local copy will be returned instead of performing the analysis
# from scratch.
#
lir_cache = dict()


class BaseDebuggerException(Exception):
    """Debugger exception class."""
    pass


class BaseDebugger(object):
    """Debugger base class with methods common to all supported debuggers.

    Every new debugger supported must derive from this class to avoid
    debugger specific functions in the decompiler code.

    """
    __metaclass__ = abc.ABCMeta

    SUPPORTED_ARCHITECTURES_NAMES = {PPC_ARCH: "PowerPC",
                                     MIPS_ARCH: "MIPS",
                                     ARM_ARCH: "ARM",
                                     AARCH64_ARCH: "AArch64",
                                     X86_ARCH: "x86",
                                     X86_64_ARCH: "x86_64"}

    def __init__(self):
        """Instance initialization."""
        # Generate verbose output when debugging flag is activated.
        self._debug = True

        # This variable contains the debugger instance in case that the current
        # debugger has to be accessed through class methods instead of
        # functions.
        self.debugger = None

        global lir_cache
        self._lir_cache = lir_cache

    @property
    def _lir_cache(self):
        """Return the current LIR cache store."""
        return self.__lir_cache

    @_lir_cache.setter
    def _lir_cache(self, _lir_cache):
        """Store the current LIR cache store."""
        self.__lir_cache = _lir_cache

    def _post_init(self):
        """Additional initializations."""
        self.unimplemented_types = self.current_arch.UNIMPLEMENTED_TYPES
        self.conditional_branch_types = self.current_arch.CONDITIONAL_BRANCH_TYPES
        self.unconditional_branch_types = self.current_arch.UNCONDITIONAL_BRANCH_TYPES
        self.assignment_types = self.current_arch.ASSIGNMENT_TYPES

    def get_group(self, _type):
        """Return the group which the instruction belongs to according to its
        type.

        """
        if _type in self.assignment_types:
            return 0
        elif _type in self.conditional_branch_types:
            return 1
        elif _type in self.unconditional_branch_types:
            return 2
        else:
            return 3

    @property
    def instruction_set(self):
        """Return the current instruction set based on the architecture in
        use.
        
        """
        return self.__instruction_set

    @instruction_set.setter
    def instruction_set(self, new_set):
        """Store the current instruction set based on the architecture in
        use.
        
        """
        self.__instruction_set = new_set

    @abc.abstractmethod
    def supported_archs(self):
        """Return a list of the supported architectures by the current
        debugger.

        """
        return

    @abc.abstractmethod
    def screen_address(self):
        """Return the effective memory address under the cursor."""
        return

    @abc.abstractmethod
    def architecture(self):
        """Return the current architecture in use."""
        return

    @property
    def architecture_name(self):
        """Return the name of the current architecture in use."""
        arch = self.SUPPORTED_ARCHITECTURES_NAMES.get(self.architecture, None)
        if arch:
            return arch

        raise BaseDebuggerException(
            "Current architecture not supported: %s" % self.architecture)

    @abc.abstractmethod
    def debugger_name(self):
        """Return the name of the debugger application."""
        return

    @abc.abstractmethod
    def get_input_file(self):
        """Return the name of the file being disassembled."""
        return

    @abc.abstractmethod
    def get_current_function_name(self):
        """Return the name of the current function under the cursor."""
        return

    @abc.abstractmethod
    def get_function_name(self, address):
        """Get the name of the function at the specified memory address."""
        return

    @abc.abstractmethod
    def get_address_label(self, address):
        """Return the label for the specified address."""
        return

#    @abc.abstractmethod
#    def get_function_instructions_addresses(self, address):
#        """Obtain the list of every instruction address inside the current
#        function.
#        This includes addresses from instructions on chunk tails.
#
#        """
#        return
#
    @abc.abstractmethod
    def get_instruction(self, address):
        """Return the instruction at the specified address."""
        return

    @abc.abstractmethod
    def get_string(self, ea, length=-1, strtype=None):
        """Get string contents."""
        return

    @abc.abstractmethod
    def get_default_compiler(self):
        """Return the default compiler for the current module."""
        return

    @abc.abstractmethod
    def get_compiler_name(self, comp):
        """Return the name of the compiler type specified."""
        return

    @abc.abstractmethod
    def display_warning(self, *args):
        """Display a warning message box to the user with the specified text.

        """
        return

    @abc.abstractmethod
    def get_frame_size(self, func_address):
        """Return the frame size of the function containing the specified
        address.
        
        """
        return

    @abc.abstractmethod
    def get_mnemonic(self, inst_address):
        """Return the mnemonic for the specified instruction address."""
        return

    @abc.abstractmethod
    def log(self, message):
        """Display a line of text in the log window."""
        return

    @abc.abstractmethod
    def perform_control_flow_graph_recovery(self, function_address):
        """Analyze every instruction and operand and it's references in the
        current function and generate a Low Level IR equivalent with them. Add
        every instruction to the generated flow chart as part of the initial
        CFG.

        This is specific to the disassembler engine where the decompiler is run
        into.
        """
        return

    def generate_lir(self, function_address):
        """
        Based on the low level instruction previously obtained by the
        disassembler layer, proceed to create a LIR representation of the
        current function under analysis.

        """
        # Check if the cache already has the requested function and return it
        # in cae it does.
        lir_function = self._lir_cache.get(function_address, None)
        if lir_function:
            return lir_function

        #
        # Get every instruction with it's operands and basic blocks
        # information and generate the Low level IR (aka LIR).
        #
        lir_function = self.perform_control_flow_graph_recovery(function_address)

        #
        # Update the cache with the newly created function.
        #
        self._lir_cache[function_address] = lir_function

        if not lir_function.is_extern:
            #
            # Perform a basic check on newly generated LIR function.
            #
            change = True
            N = list()
            lir_function[0].dom.add(lir_function[0])

            for lir_bb in lir_function[1 : ]:
                lir_bb.dom = set(copy(lir_function.basic_blocks))

            #for n in lir_function[1:]:
            succ_list = list()
            cur_node = lir_function[0]
            #succ_list.add(cur_node)

            def get_successors_list(cur_node, level):

                #print "%s ID : %d - successors %d" % (
                #    "  " * level, cur_node.id, len(cur_node.successors()))
                if cur_node.visited:
                    #print "ALREADY visited", cur_node.id
                    return list()

                cur_node.visited = True
                level += 1

                cur_list = list()
                cur_list.append(cur_node)

                for succ in cur_node.successors():
                    cur_list.append(succ)
                    #print "%s +---> succ node : %d (0x%X)" % (
                    #    "  " * level, succ.id, succ.start_address)
                    cur_list += get_successors_list(succ, level)

                #print "level %d - %s" % (level, [x.id for x in cur_list])
                level -= 1
                return cur_list

            level = 0
            succ_list += get_successors_list(cur_node, level)
            #raise Exception("blablabla")

            purged_succ_list = list()
            for x in succ_list:
                if x not in purged_succ_list:
                    purged_succ_list.append(x)

            while change is True:

                print "purged_succ_list = ", [x.id for x in purged_succ_list]
                for n in purged_succ_list[1:]:

                    #T = set(copy(lir_function.basic_blocks))
                    #T = sorted(succ_list)
                    #T = succ_list
                    T = set(purged_succ_list)
                    print "T = ", [x.id for x in sorted(T)]

                    #print "n = ", n.id
                    #print "   preds = ", [x.id for x in n.predecessors()]

                    for i, p in enumerate(n.predecessors()):
                        print "p (n.pred #%d) = %d" % (i, p.id)
                        #print "n --->", [x.id for x in n.dom]
                        print "p --->", [x.id for x in p.dom]
                        print "----> intersection = ", [x.id for x in T.intersection(p.dom)]
                        #break
                        T.intersection_update(p.dom)

                    D = set()
                    D.add(n)
                    D.update(T)

                    print " D :=", [x.id for x in D]

                    if D != n.dom:
                        change = True
                        n.dom = D
                    else:
                        change = False

            print "---------------------------------------------"
            print "      i                Domin(i)"
            print "---------------------------------------------"
            for lir_bb in lir_function:
                print "    0x%08X {%2d}    {%s}" % (
                    lir_bb.start_address, lir_bb.id, ", ".join(
                    [str(x.id) for x in lir_bb.dom]))

            if lir_function.get_basic_blocks_count() == 0:
                raise BaseDebuggerException(
                    "No basic blocks found during the analysis.")

            if lir_function.instructions_count == 0:
                raise BaseDebuggerException(
                    "No instructions found during the analysis.")
            raise Exception("blablabla")

            try:
                #print "[+] Generating DU and UD chains for Low level IR..."
                lir_function.generate_chains()
            except Exception, err:
                #print format_exc()
                raise BaseDebuggerException(err)

        return lir_function

    @abc.abstractmethod
    def display_boxed_message(self, message):
        """Display a boxed message with a cancel button in it."""
        return

    @abc.abstractmethod
    def hide_boxed_message(self):
        """Hide a boxed message being displayed."""
        return

    @abc.abstractmethod
    def dword(self, address):
        """Return the dword at the specified address."""
        return
