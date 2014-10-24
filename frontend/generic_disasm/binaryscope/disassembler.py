# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from base import *

import bsapi
#try:
#    import bsapi
#except ImportError, err:
#    raise BaseDebuggerException("Binary scope is not supported")

raise Exception("UNCOMMONT THE FOLLOWING LINES")
#from frontend.lir.lir_instruction import LowLevelInstruction
#from frontend.lir.lir_basicblock import LowLevelBasicBlock
#from frontend.lir.lir_function import LowLevelFunction
#from frontend.lir.lir_operand import LowLevelOperand

__all__ = ["Disassembler", "DisassemblerException"]


class DisassemblerException(BaseDebuggerException):
    """Binary scope exception class."""
    pass


class Disassembler(BaseDebugger):
    """Debugger specific functions for the Binary scope Disassembler from
    the awesome team of Sebastian Muniz ;)
    
    """

    DEBUGGER_NAME = "Binary scope Disassembler"

    # Currently supported architectures by this debugger.
    SUPPORTED_ARCHS = [PPC_ARCH, MIPS_ARCH, ARM_ARCH, X86_ARCH, X86_64_ARCH]

    # These are copy of Binary Scope internal definitions.
    __POWERPC_ARCHITECTURE = "POWERPC"
    __MIPS_ARCHITECTURE = "MIPS"
    __ARM_ARCHITECTURE = "ARM"
    __X86_ARCHITECTURE = "I386"

    STRING_TYPE_C = 0       # C-style ASCII string
    STRING_TYPE_PASCAL = 1  # Pascal-style ASCII string (length byte)
    STRING_TYPE_LEN2 = 2    # Pascal-style, length is 2 bytes
    STRING_TYPE_UNICODE = 3 # Unicode string
    STRING_TYPE_LEN4 = 4    # Pascal-style, length is 4 bytes
    STRING_TYPE_ULEN2 = 5   # Pascal-style Unicode, length is 2 bytes
    STRING_TYPE_ULEN4 = 6   # Pascal-style Unicode, length is 4 bytes
    STRING_TYPE_LAST = 7    # Last string type

    COMPILER_UNK = 0        # Unknown
    COMPILER_MS = 1         # Visual C++
    COMPILER_BC = 2         # Borland C++
    COMPILER_WATCOM = 3     # Watcom C++
    COMPILER_GNU = 4        # GNU C++
    COMPILER_VISAGE = 5     # Visual Age C++
    COMPILER_BP = 6         # Delphi

    def __init__(self):
        """Instance initialization."""
        super(Disassembler, self).__init__()
        #
        # Set architecture specific types for the current binary being
        # analyzed.
        #
        architecture = self.get_architecture()

        if architecture is PPC_ARCH:
            import powerpc as current_arch

        elif architecture is MIPS_ARCH:
            import mips as current_arch

        elif architecture is ARM_ARCH:
            import arm as current_arch

        elif architecture in X86_ARCH:
            import x86 as current_arch

        elif architecture is X86_64_ARCH:
            import x86_64 as current_arch

        self.current_arch = current_arch
        self.instruction_set = current_arch.InstructionSet

        # Perform additional initializations.
        self._post_init()

    def get_screen_address(self):
        """Return the effective memory address under the cursor."""
        return bsapi.get_screen_address()

    def get_architecture(self):
        """Return the current architecture in use."""
        architecture_name = bsapi.get_architecture_name()

        if not architecture_name:
            raise DisassemblerException(
                "Unable to obtain an architecture name")

        if architecture_name == self.__POWERPC_ARCHITECTURE:
            return PPC_ARCH
        elif architecture_name == self.__MIPS_ARCHITECTURE:
            return MIPS_ARCH
        elif architecture_name == self.__ARM_ARCHITECTURE:
            return ARM_ARCH
        elif architecture_name == self.__X86_ARCHITECTURE:
            if bsapi.get_machine_name() == "":
                return X86_ARCH
            else:
                return X86_ARCH_64

        raise DisassemblerException(
            "Unsupported architecture %s" % architecture_name)

    def get_input_file(self):
        """Return the name of the file being disassembled."""
        return bsapi.get_root_filename()

    def get_current_function_name(self):
        """Return the name of the current function under the cursor."""
        return self.get_function_name(self.get_screen_address())

    def get_function_name(self, address):
        """Get the name of the function at the specified memory address."""
        name = bsapi.get_function_name(address)

        if name is not None:
            return name

        raise DisassemblerException(
            "Unable to obtain function name for address 0x%X" % address)

    def get_address_label(self, address):
        """Return the label for the specified address."""
        return get_name(address, address)

    def get_function_instructions_addresses(self, address):
        """Obtain the list of every instruction address inside the current
        function.

        This includes addresses from instructions on chunk tails.

        :param address: An address pertaining to the function.
        """
        function_instructions = list()  # Collecting function chunks

        # Get the tail iterator
        function = bsapi.get_function(address)

        for basic_block in function.basic_blocks:

            # Go through all instructions in the basic block
            # and add their addresses to our list.
            for inst_addr, inst_disasm in basic_block:
                function_instructions.append(inst_addr)

        return function_instructions

    def get_instruction_length(self, address):
        """Return the length of the instruction at the specified address."""
        return decode_insn(address)

    def set_operand_info(self, lir_op, op):
        """Store operand information from the operands at the current
        instruction.

        """
        if op is None:
            # Below sets are set by default so no need to do it again.
            #lir_op.type(o_void) # no operand
            #lir_op.number(0)
            return False

        # Retrieve operand value according to it's type
        if op.type == o_void:
            return False # no operand

        elif op.type in [o_mem, o_far, o_near]:
            value = op.addr

        elif op.type == o_displ:
            #print "disp r%d + offset 0x%X" % (op.phrase, op.addr)
            value = [op.phrase, op.addr]

        elif op.type == o_reg:
            value = op.reg

        elif op.type == o_imm:
            value = op.value

        elif op.type == o_phrase:
            value = op.phrase

        else:
            # TODO : check for architecture specific operands.
            #raise DisassemblerException("Unrecognized operand type %d" % op.type)
            value = None

        # Retrieve operand number and type
        lir_op.type = op.type
        lir_op.number = op.n

        lir_op.value = value

        return True

    def get_instruction_operand(self, address, operand_index):
        """Return the operand information in an instruction for the spedified
        operand number.
        
        """
        try:
            inslen = decode_insn(address)

            if inslen == 0:
                return None

            #insn = get_current_instruction() # <- deprecated? comment by topo 2013
            insn = cvar.cmd

            if not insn:
                return None

            op = get_instruction_operand(insn, operand_index)

        except Exception, err:
            #print err
            inslen = decode_insn(address)
            # inslen = decode_insn(lir_inst.ea) # Commented by topo 2013

            if inslen == 0:
                return None

            op = cmd.Operands[operand_index]

        return op

    def set_instruction_info(self, lir_inst, instruction):
        """Obtain instruction and operand information from the current debugger
        instance.

        """
        #lir_inst.is_macro   = False #instruction.is_macro()
        lir_inst.address = instruction.address
        lir_inst.type = instruction.type
        lir_inst.mnemonic = instruction.mnemonic

        # Parse every operand present in the instruction being analyzed
        for operand_index in xrange(bsapi.MAX_OPERANDS):
            inst_operand = \
                self.get_instruction_operand(instruction.ea, operand_index)

            #print "%d" % inst_operand.type
            if not inst_operand:
                break

            lir_operand = LowLevelOperand()

            #print "ea 0x%X has operand idx %d - ty %d val %d" % \
            #    (instruction.ea, operand_index, inst_operand.type,
            #    inst_operand.value)

            if not self.set_operand_info(lir_operand, inst_operand):
                break

            lir_inst.operands.append(lir_operand)

        return True

    def get_instruction(self, address):
        """Return the instruction at the specified address."""
        return DecodeInstruction(address)

    def get_string(self, ea, length=None, strtype=STRING_TYPE_C):
        """Get string contents.

        @param ea: linear address
        @param length: string length. -1 means to calculate the max string length
        @param strtype: the string type (one of ASCSTR_... constants)

        @return: string contents or empty string

        """
        if length is None:
            length = bsapi.get_max_ascii_length(ea, strtype)

        return bsapi.get_ascii_contents(ea, length, strtype)

    def get_default_compiler(self):
        """Return the default compiler for the current module."""
        return default_compiler()

    def get_compiler_name(self, comp):
        """Return the name of the compiler type specified."""
        return get_compiler_name(comp)

    def display_warning(self, *args):
        """Display a warning message box to the user with the specified text.
        
        """
        warning(*args)

    def get_frame_size(self, func_address):
        """Return the frame size of the function containing the specified
        address.
        
        """
        return GetFrameLvarSize(func_address)

    def get_mnemonic(self, inst_address):
        """Return the mnemonic for the specified instruction address."""
        return GetMnem(inst_address)

    def log(self, message):
        """Display a line of text in the log window."""
        # TODO / FIXME
        print str(message)

    def generate_lir(self, func_address):
        """Analyze every instruction and operand and it's references in the
        current function and generate a low level IR equivalent with them.

        """
        # Obtain function scope if available.
        func = bsapi.get_function(func_address)

        if not func:
            raise DisassemblerException(
                "Unable to obtain function object for address 0x%X" %
                func_address)

        #
        # Create a LIR function and start filling it with the basic blocks
        # and its pertaining instructions.
        #
        lir_function = LowLevelFunction()

        if not lir_function.set_source_function_info(
            func.start_address,
            func.end_address,
            self.get_function_name(func.start_address)):

            raise DisassemblerException(
                "Could not obtain function information for address 0x%X" %
                func_address)

        # We'll create a list of instruction instances and also check for
        # basic blocks boundaries.
        current_basic_block = None

        # Obtain all the instructions that compose the function being analyzed
        # (including the ones in chunks).
        instructions = self.get_function_instructions_addresses(func_address)

        for index, ea in enumerate(instructions):

            in_edges = dict()

            #print "[!] Discovered basic block number %d " \
            #      "at address 0x%X" % (len(lir_function.basic_blocks), ea)

            current_basic_block = LowLevelBasicBlock(ea)

            lir_function.add_basic_block(current_basic_block)

            # Add every edge found to the list belonging to that basic
            # block
            for in_ref_type in in_edges:

                #print "    0x%X has Ref type %s : %s " % \
                #      (ea, XrefTypeName(in_ref_type),
                #       [hex(x) for x in in_edges[in_ref_type]])

                for in_edge in in_edges[in_ref_type]:
                    current_basic_block.add_in_edge(in_edge)

            # Store the current instruction into a low level intermediate
            # representation instance along with the basic block information
            # for the current function being decompiled.
            inst = bsapi.decode_instruction(ea)

            if not inst:
                raise DisassemblerException(
                    "Unable to decode instruction at 0x%08X" % ea)

            # Analyze the instruction obtained by the debugger and then add the
            # current instruction to the basic block being processed.
            lir_inst = LowLevelInstruction()

            if not self.set_instruction_info(lir_inst, inst):
                raise DisassemblerException(
                    "Unable to store information for instruction at 0x%08X" %
                    ea)

            current_basic_block.add_instruction(ea, lir_inst)

        return lir_function
