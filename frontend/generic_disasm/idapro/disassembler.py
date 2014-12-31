# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from ..base import *

try:
    import idaapi
except ImportError, err:
    raise BaseDebuggerException("IDA Pro is not supported")

from idaapi import *
from idc import *
from idautils import *

from misc.prerequisites import require as req_

req_("frontend.lir.lir_instruction")
from frontend.lir.lir_instruction import LowLevelInstruction

req_("frontend.lir.lir_basicblock")
from frontend.lir.lir_basicblock import LowLevelBasicBlock

req_("frontend.lir.lir_function")
from frontend.lir.lir_function import LowLevelFunction

req_("frontend.lir.lir_operand")
import frontend.lir.lir_operand
reload(frontend.lir.lir_operand)
from frontend.lir.lir_operand import LowLevelOperand, OPERAND_TYPES

__all__ = ["Disassembler", "DisassemblerException"]


class DisassemblerException(BaseDebuggerException):
    """IDA Pro exception class."""
    pass


class Disassembler(BaseDebugger):
    """Debugger specific functions for the IDA Pro Disassembler from
    Hex-Rays.
    
    """

    DEBUGGER_NAME = "IDA Pro Disassembler"


    STRING_TYPE_C = ASCSTR_TERMCHR # C-style ASCII string
    STRING_TYPE_PASCAL = ASCSTR_PASCAL  # Pascal-style ASCII string (length byte)
    STRING_TYPE_LEN2 = ASCSTR_LEN2    # Pascal-style, length is 2 bytes
    STRING_TYPE_UNICODE = ASCSTR_UNICODE # Unicode string
    STRING_TYPE_LEN4 = ASCSTR_LEN4    # Pascal-style, length is 4 bytes
    STRING_TYPE_ULEN2 = ASCSTR_ULEN2   # Pascal-style Unicode, length is 2 bytes
    STRING_TYPE_ULEN4 = ASCSTR_ULEN4   # Pascal-style Unicode, length is 4 bytes
    STRING_TYPE_LAST = ASCSTR_LAST    # Last string type

    COMPILER_UNK = COMP_UNK       # Unknown
    COMPILER_MS = COMP_MS        # Visual C++
    COMPILER_BC = COMP_BC        # Borland C++
    COMPILER_WATCOM = COMP_WATCOM    # Watcom C++
    COMPILER_GNU = COMP_GNU       # GNU C++
    COMPILER_VISAGE = COMP_VISAGE    # Visual Age C++
    COMPILER_BP = COMP_BP        # Delphi

    #
    # instruc_t.feature
    #
    FEATURE_STOP = CF_STOP  #  Instruction doesn't pass execution to the next instruction
    FEATURE_CALL = CF_CALL  #  CALL instruction (should make a procedure here)
    FEATURE_CHG1 = CF_CHG1  #  The instruction modifies the first operand
    FEATURE_CHG2 = CF_CHG2  #  The instruction modifies the second operand
    FEATURE_CHG3 = CF_CHG3  #  The instruction modifies the third operand
    FEATURE_CHG4 = CF_CHG4  #  The instruction modifies 4 operand
    FEATURE_CHG5 = CF_CHG5  #  The instruction modifies 5 operand
    FEATURE_CHG6 = CF_CHG6  #  The instruction modifies 6 operand
    FEATURE_USE1 = CF_USE1  #  The instruction uses value of the first operand
    FEATURE_USE2 = CF_USE2  #  The instruction uses value of the second operand
    FEATURE_USE3 = CF_USE3  #  The instruction uses value of the third operand
    FEATURE_USE4 = CF_USE4  #  The instruction uses value of the 4 operand
    FEATURE_USE5 = CF_USE5  #  The instruction uses value of the 5 operand
    FEATURE_USE6 = CF_USE6  #  The instruction uses value of the 6 operand
    FEATURE_JUMP = CF_JUMP  #  The instruction passes execution using indirect jump or call (thus needs additional analysis)
    FEATURE_SHFT = CF_SHFT  #  Bit-shift instruction (shl,shr...)
    FEATURE_HLL  = CF_HLL   #  Instruction may be present in a high level language function.

    #
    # Instruction features supported.
    #
    FEATURES_TRANSLATION = {
        CF_STOP : FEATURE_STOP,
        CF_CALL : FEATURE_CALL,
        CF_CHG1 : FEATURE_CHG1,
        CF_CHG2 : FEATURE_CHG2,
        CF_CHG3 : FEATURE_CHG3,
        CF_CHG4 : FEATURE_CHG4,
        CF_CHG5 : FEATURE_CHG5,
        CF_CHG6 : FEATURE_CHG6,
        CF_USE1 : FEATURE_USE1,
        CF_USE2 : FEATURE_USE2,
        CF_USE3 : FEATURE_USE3,
        CF_USE4 : FEATURE_USE4,
        CF_USE5 : FEATURE_USE5,
        CF_USE6 : FEATURE_USE6,
        CF_JUMP : FEATURE_JUMP,
        CF_SHFT : FEATURE_SHFT,
        CF_HLL  : FEATURE_HLL 
        }

    FEATURES_STR = {
        FEATURE_STOP : "CF_STOP",
        FEATURE_CALL : "CF_CALL",
        FEATURE_CHG1 : "CF_CHG1",
        FEATURE_CHG2 : "CF_CHG2",
        FEATURE_CHG3 : "CF_CHG3",
        FEATURE_CHG4 : "CF_CHG4",
        FEATURE_CHG5 : "CF_CHG5",
        FEATURE_CHG6 : "CF_CHG6",
        FEATURE_USE1 : "CF_USE1",
        FEATURE_USE2 : "CF_USE2",
        FEATURE_USE3 : "CF_USE3",
        FEATURE_USE4 : "CF_USE4",
        FEATURE_USE5 : "CF_USE5",
        FEATURE_USE6 : "CF_USE6",
        FEATURE_JUMP : "CF_JUMP",
        FEATURE_SHFT : "CF_SHFT",
        FEATURE_HLL  : "CF_HLL"
        }

    def __init__(self):
        """Instance initialization."""
        super(Disassembler, self).__init__()
        #
        # Set architecture specific types for the current binary being
        # analyzed.
        #
        architecture = self.architecture

        if architecture is PPC_ARCH:
            import powerpc32 as current_arch

        elif architecture is MIPS_ARCH:
            import mips as current_arch

        elif architecture is ARM_ARCH:
            import arm as current_arch

        elif architecture is X86_ARCH:
            import x86 as current_arch

        self.current_arch = current_arch
        self.instruction_set = current_arch.InstructionSet()

        # Perform additional initializations.
        self._post_init()

    @property
    def debugger_name(self):
        """Return the name of the debugger application."""
        return self.DEBUGGER_NAME

    @property
    def supported_archs(self):
        """Return a list of the supported architectures by the current
        debugger.

        """
        return self.SUPPORTED_ARCHS

    @property
    def screen_address(self):
        """Return the effective memory address under the cursor."""
        return get_screen_ea()

    @property
    def architecture(self):
        """Return the current architecture in use."""
        processor_name = get_idp_name()

        # Convert IDA architectures IDs to our own.
        if processor_name == "ppc":
            return PPC_ARCH
        elif processor_name == "mips":
            return MIPS_ARCH
        elif processor_name == "arm":
            return ARM_ARCH
        elif processor_name == "pc":
            return X86_ARCH

        raise DisassemblerException(
            "Unsupported architecture %s" % processor_name)

    def get_input_file(self):
        """Return the name of the file being disassembled."""
        return get_root_filename()

    def get_current_function_name(self):
        """Return the name of the current function under the cursor."""
        return self.get_function_name(self.screen_address)

    def get_current_function_address(self):
        """Return the address of the current function under the cursor."""
        func = get_func(self.screen_address)

        if not func:
            raise DisassemblerException(
                "No function present at 0x%08X" % self.screen_address)

        return func.startEA

    def get_function_name(self, address):
        """Get the name of the function at the specified memory address."""
        name = get_func_name(address)

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
        func_iter = func_tail_iterator_t(get_func(address))

        # While the iterator status is valid
        status = func_iter.main()

        while status:
            # Get the chunk
            chunk = func_iter.chunk()

            # Go through all instructions in the basic block
            # and add their addresses to our list.
            for head in Heads(chunk.startEA, chunk.endEA):
                if isCode(getFlags(head)):
                    function_instructions.append(head)

            # Get the last status
            status = func_iter.next()

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
            value = [op.phrase, op.addr]

        elif op.type == o_reg:
            value = op.reg

        elif op.type == o_imm:
            value = op.value

        elif op.type == o_phrase:
            value = op.phrase

        else:
            value = op.value

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
        #lir_inst.is_macro = False #instruction.is_macro()
        lir_inst.address = instruction.ea
        lir_inst.type = instruction.itype
        lir_inst.mnemonic = self.get_mnemonic(instruction.ea) if self._debug else None
        lir_inst.group = self.get_group(lir_inst.type)
        lir_inst._aux = instruction.auxpref
        lir_inst.features = [f_v for f_k, f_v in self.FEATURES_TRANSLATION.iteritems() \
                    if f_k & instruction.get_canon_feature() == f_k]

        # Display instruction information obtained form IDA internals.
        if False:
            feature_str = ", ".join(
                [f_v for f_k, f_v in self.FEATURES_STR.iteritems() \
                    if f_k in lir_inst.features])

            inst_str = "0x%08X : %-3d %+5s - aux %-5d - seg %-5d - insn %-5d - flag %-5d - fea %s" % (
                lir_inst.address,
                lir_inst.type,
                lir_inst.mnemonic,
                instruction.auxpref,
                instruction.segpref,
                instruction.insnpref,
                instruction.flags,
                feature_str)
            print inst_str

        # Parse every operand present in the instruction being analyzed
        for operand_index in xrange(UA_MAXOP):
            #inst_operand = \
            #    self.get_instruction_operand(instruction.ea, operand_index)
            inst_operand = instruction.Operands[operand_index]

            if not inst_operand or inst_operand.type is o_void:
                break

            # Create a new operand representation and pass the registers names
            # table so the instance can translate registers numbers to its
            # string representation.
            lir_op = LowLevelOperand(
                self.instruction_set.GPR_NAMES, self.instruction_set.SPR_NAMES)

            #print "\tidx %d (n %d) - ty %d val %d" % \
            #    (operand_index, inst_operand.n,
            #    inst_operand.type, inst_operand.value)

            if not self.set_operand_info(lir_op, inst_operand):
                break

            lir_inst.operands.append(lir_op)

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
            length = get_max_ascii_length(ea, strtype)

        return get_ascii_contents(ea, length, strtype)

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
        try:
            return GetDisasm(inst_address).split()[0]
        except IndexError, err:
            return None
        #return ua_mnem(inst_address)

    def log(self, message):
        """Display a line of text in the log window."""
        print str(message)

    def _generate_lir(self, func_address):
        """Analyze every instruction and operand and it's references in the
        current function and generate a low level IR equivalent with them.

        """
        # Obtain function scope if available.
        func = get_func(func_address)

        if not func:
            raise DisassemblerException(
                "Unable to obtain function object for address 0x%X" %
                func_address)

        #
        # Create a LIR function and start filling it with the basic blocks
        # and its pertaining instructions.
        #
        lir_function = LowLevelFunction(
            func.startEA,
            func.endEA,
            self.get_function_name(func.startEA),
            self.instruction_set)

        dones = {}
        for basic_block in FlowChart(func):

            ea = basic_block.startEA
            current_basic_block = LowLevelBasicBlock(ea)

            lir_function.add_basic_block(current_basic_block)

            for inst_ea in list(Heads(basic_block.startEA, basic_block.endEA)):
                lir_inst = LowLevelInstruction()

                if not self.set_instruction_info(lir_inst, self.get_instruction(inst_ea)):
                    raise DisassemblerExceptior(
                        "Unable to store information for instruction at 0x%08X" %
                        ea)

                current_basic_block.add_instruction(inst_ea, lir_inst)

        return lir_function

    def display_boxed_message(self, message):
        """Display a boxed message with a cancel button in it."""
        show_wait_box(message)

    def hide_boxed_message(self):
        """Hide a boxed message being displayed."""
        hide_wait_box()
