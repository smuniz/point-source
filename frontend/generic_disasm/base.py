# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc

__all__ = ["BaseDebugger",
           "BaseDebuggerException",
           "PPC_ARCH",
           "MIPS_ARCH",
           "ARM_ARCH",
           "X86_ARCH",
           "X86_64_ARCH"]

PPC_ARCH = 0
MIPS_ARCH = 1
ARM_ARCH = 2
X86_ARCH = 3
X86_64_ARCH = 4

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
                                     X86_ARCH: "x86",
                                     X86_64_ARCH: "x86_64"}

    def __init__(self):
        """Instance initialization."""
        # Generate verbose output when debugging flag is activated.
        self.__debug = True

        # This variable contains the debugger instance in case that the current
        # debugger has to be accessed through class methods instead of
        # functions.
        self.debugger = None

        self.__check_attribute("SUPPORTED_ARCHS")
        self.__check_attribute("DEBUGGER_NAME")

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

    def __check_attribute(self, attribute_name):
        """Perform a check on the specified attribute name and raise an
        exception in case it's missing."""
        if not hasattr(self, attribute_name):
            raise BaseDebuggerException(
                "Debugger class %s has missing \"%s\" attribute." %
                (self.__class__.__name__, attribute_name))

    @property
    @abc.abstractmethod
    def screen_address(self):
        """Return the effective memory address under the cursor."""
        return

    @property
    @abc.abstractmethod
    def architecture(self):
        """Return the current architecture in use."""
        return

    @property
    def architecture_name(self):
        """Return the name of the current architecture in use."""
        try:
            return self.SUPPORTED_ARCHITECTURES_NAMES[self.architecture]
        except IndexError, err:
            raise BaseDebuggerException(
                "Current architecture not supported: %s" % err)

    @property
    def debugger_name(self):
        """Return the name of the debugger application."""
        return self.DEBUGGER_NAME

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

    @abc.abstractmethod
    def get_function_instructions_addresses(self, address):
        """Obtain the list of every instruction address inside the current
        function.
        This includes addresses from instructions on chunk tails.

        """
        return

    @abc.abstractmethod
    def is_basic_block_start_address(self, ea, index, in_edges, lir_function):
        """..."""
        return

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
    def set_instruction_info(self, lir_inst, instruction):
        """Obtain instruction and operand information from the current debugger
        instance.

        """
        return

    @abc.abstractmethod
    def log(self, message):
        """Display a line of text in the log window."""
        return

    @abc.abstractmethod
    def generate_lir(self, func_address):
        """Analyze every instruction and operand and it's references in the
        current function and generate a low level IR equivalent with them.

        """
        return
