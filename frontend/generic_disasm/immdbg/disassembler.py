# 
# Copyright (c) 2013 Sebastian Muniz
#
# This code is part of point source decompiler
#

from base import *

try:
    import immlib
except ImportError, err:
    raise BaseDebuggerException("Immunity debugger is not supported.")

from immlib import Debugger, Register

__all__ = ["Disassembler", "DisassemblerException"]


class DisassemblerException(BaseDebuggerException):
    """Immunity debugger exception class."""
    pass


class Disassembler(BaseDebugger):
    """Debugger specific functions for the Immunity debugger from Immunity
    Inc.
    
    """

    DEBUGGER_NAME = "Immunity Debugger"

    # Currently supported architectures by this debugger.
    SUPPORTED_ARCHS = [X86_ARCH]

    def __init__(self):
        """Instance initialization."""
        super(Disassembler, self).__init__()
        #
        # Set architecture specific types for the current binary being
        # analyzed.
        #
        architecture = self.get_architecture()

        if architecture is X86_ARCH:
            import x86 as current_arch

        self.current_arch = current_arch
        self.instruction_set = current_arch.InstructionSet

        # Perform additional initializations.
        self._post_init()

        self.debugger = Debugger()

    def get_screen_address(self):
        """Return the effective memory address under the cursor."""
        # I was unable to find a way to determine current cursor position in
        # the screen so I ended using the EIP register address because imdbg
        # should have it set while running. This makes impossible to decompile
        # an offline application.
        if self.debugger.isRunning() or self.debugger.isEvent() or \
                self.debugger.isStopped():
            return self.debugger.getRegs()["EIP"]

        raise ImmunityDebuggerException(
            "Debugger must be running to execute")

    def get_architecture(self):
        """Return the current architecture in use."""
        return X86_ARCH

    def get_input_file(self):
        """Return the name of the file being disassembled."""
        return self.debugger.getDebuggedName()

    def get_current_function_name(self):
        """Return the name of the current function under the cursor."""
        self._raise(self.get_current_function_name)

    def get_function_name(self, address):
        """Get the name of the function at the specified memory address."""
        self._raise(self.get_function_name)

    def get_address_label(self, address):
        """Return the label for the specified address."""
        self._raise(self.get_address_label)

    def get_function_instructions_addresses(self, address):
        """Obtain the list of every instruction address inside the current
        function.
        This includes addresses from instructions on chunk tails.

        """
        self._raise(self.get_function_instructions_addresses)

    def is_basic_block_start_address(self, ea, index, in_edges, lir_function):
        """..."""
        self._raise(self.is_basic_block_start_address)

    def generate_lir(self, func_address):
        """Analyze every instruction and operand and it's references in the
        current function and generate a low level IR equivalente with them.

        """
        # Obtain function scope if available.
        func = self.debugger.getFunction(func_address)

        if not func:
            raise ImmunityDebuggerException(
                "Unable to obtain function object for address 0x%X" %
                func_address)

        try:
            bbs = func.getBasicBlocks()
        except Exception, err:
            raise ImmunityDebuggerException(
                "Unable to obtain basic blocks for function at address 0x%X" \
                "- %s" % (func_address, err))

        bbmap = dict()
        cfg = dict()

        """
        #Make a control flow graph
        for bb in bbs:
            cfg[bb.getStart()] = bb.getEdges()

        #Make a hash of each BB
        for bb in bbs:
            bbhash_data = []
            for op in bb.get_instructions(self.imm):
                #take into account just information about the opcode
                instr = []
                instr.append(op.getMemType())
                instr.append(op.indexed)
                instr.append(op.getCmdType())
                instr.append(op.optype[0])
                instr.append(op.optype[1])
                instr.append(op.optype[2])
                instr.append(op.getSize())
                bbhash_data.append(self.hash_a_list(instr))
            bbhash = self.hash_a_list(bbhash_data)
            bbmap[bb.getStart()] = bbhash
        """
        return None

    def get_instruction(self, address):
        """Return the instruction at the specified address."""
        self._raise(self.get_instruction)

    def get_string(self, ea, length=-1, strtype=None):
        """Get string contents."""
        self._raise(self.get_string)

    def get_default_compiler(self):
        """Return the default compiler for the current module."""
        self._raise(self.get_default_compiler)

    def get_compiler_name(self, comp):
        """Return the name of the compiler type specified."""
        self._raise(self.get_compiler_name)

    def display_warning(self, *args):
        """Display a warning message box to the user with the specified text.

        """
        self._raise(self.display_warning)

    def get_frame_size(self, func_address):
        """Return the frame size of the function containing the specified
        address.
        
        """
        self._raise(self.get_frame_size)

    def get_mnemonic(self, inst_address):
        """Return the mnemonic for the specified instruction address."""
        self._raise(self.get_mnemonic)

    def set_instruction_info(self, instruction):
        """Obtain instruction and operand information from the current debugger
        instance.

        """
        self._raise(self.set_instruction_info)

    def log(self, message):
        """Display a line of text in the log window."""
        self.debugger.logLines(message)
        self.debugger.updateLog()
