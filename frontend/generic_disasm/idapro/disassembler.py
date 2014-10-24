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

    # Currently supported architectures by this debugger.
    SUPPORTED_ARCHS = [PPC_ARCH, MIPS_ARCH, ARM_ARCH, X86_ARCH]

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
    FEATURES = {
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
        self.instruction_set = current_arch.InstructionSet

        # Perform additional initializations.
        self._post_init()

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
        return get_func(self.screen_address).startEA

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

    def is_basic_block_start_address(self, ea, index, in_edges, lir_function):
        """..."""
        # Initialize variable to indicate that a new basic block is needed.
        create_new_basic_block = False

        # Check if current instruction is being referenced from another
        # part of the program.
        # This way we know it's the beginning of a basic block.
        #in_edges = {}
        xb = xrefblk_t()

        # Check if the first instruction of the function is the one being
        # processed. In that case always create a basic block and for check
        # for references because it could happen that the function is not
        # referenced so we could miss the basic block creation.
        if index == 0:
            create_new_basic_block = True

        elif xb.first_to(ea, XREF_ALL):

            # Discard data references, only accept code references.
            if xb.iscode:
                # TODO: function arrays and certain switch cases could fail.
                while True:

                    # Create the key for the ref type if it didn't exist.
                    # Then add the new reference to the list.
                    ref_type = xb.type

                    if not ref_type in in_edges:
                        in_edges[ref_type] = list()

                    in_edges[ref_type].append(xb.frm)

                    #print "[!] 0x%X referenced from 0x%X (type %d %s)" % \
                    #      (ea, xb.frm, xb.type, XrefTypeName(xb.type))

                    # Continue there are more references available.
                    if not xb.next_to():
                        break

            create_new_basic_block = False

            # If we find the initial instruction we don't do further
            # checks.
            if ea == lir_function.start_address:
                create_new_basic_block = True
                #print "1) 0x%X" % ea

            elif not fl_F in in_edges:  # check if not flow to the next instruction
                # We've found an instruction exclusively referenced by
                # a branch... this is definitely a basic block start
                # address.
                create_new_basic_block = True
                #print "2) 0x%X" % ea

            elif len(in_edges) == 1:
                # Flow xref... check if previous instruction was a branch?
                xb_prev = xrefblk_t()
                xrefed_by = in_edges[fl_F][0]

                if xb_prev.first_from(xrefed_by, XREF_ALL):
                    while True:
                        # By checking that the reference is inside the
                        # current function we discard data references and
                        # calls to other functions.

                        # TODO: functions arrays and special switch cases
                        # could cause a fail.
                        if xb_prev.iscode and \
                                xb_prev.to != ea and xb_prev.type in [fl_JF, fl_JN]:
                            #print "3) 0x%X - type %d - to 0x%X" % \
                            #      (xrefed_by, xb_prev.type, xb_prev.to)

                            create_new_basic_block = True

                        # Continue there are more references available.
                        if not xb_prev.next_from():
                            break

            else:
                # Instruction referenced by a flow xref but also from a
                # branch so this is the start of a basic block.
                create_new_basic_block = True
                #print "4) 0x%X" % ea

        return create_new_basic_block

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
            # TODO : check for architecture specific operands.
            #raise DisassemblerException("Unrecognized operand type %d" % op.type)
            value = op.value

        # Retrieve operand number and type
        lir_op.type = op.type   # FIXME : this just works cause we use IDA Pro
                                # operand definitions. We have to enhance this.
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
        #lir_inst.is_macro = False #instruction.is_macro()
        lir_inst.address = instruction.ea
        lir_inst.type = instruction.itype
        lir_inst.mnemonic = self.get_mnemonic(instruction.ea)

        feature_str = ", ".join(
            [f_v for f_k, f_v in self.FEATURES.iteritems() \
                if f_k & instruction.get_canon_feature() == f_k])

        inst_str = "%3d %+5s aux %-5d seg %-5d insn %-5d flag %-5d %s" % (
            lir_inst.type,
            lir_inst.mnemonic,
            instruction.auxpref,
            instruction.segpref,
            instruction.insnpref,
            instruction.flags,
            feature_str)
        lir_inst.group = self.get_group(lir_inst.type)

        # Parse every operand present in the instruction being analyzed
        for operand_index in xrange(UA_MAXOP):
            inst_operand = \
                self.get_instruction_operand(instruction.ea, operand_index)

            if not inst_operand or inst_operand.type is o_void:
                break

            # Create a new operand representation and pass the registers names
            # table so the instance can translate registers numbers to its
            # string representation.
            lir_op = LowLevelOperand(self.instruction_set.GPR_NAMES, self.instruction_set.SPR_NAMES)

            #print "ea 0x%X has operand idx %d - ty %d val %d/%d" % \
            #    (instruction.ea, operand_index, inst_operand.type,
            #    inst_operand.value, inst_operand.n)

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
        # TODO / FIXME
        print str(message)

    def generate_lir(self, func_address):
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
        lir_function = LowLevelFunction()

        if not lir_function.set_source_function_info(
            func.startEA,
            func.endEA,
            self.get_function_name(func.startEA)):

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

            if self.is_basic_block_start_address(ea, index, in_edges, lir_function):

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
            inst = DecodeInstruction(ea)

            if not inst:
                raise DisassemblerException("Empty instruction at 0x%08X" % ea)

            # Analyze the instruction obtained by the debugger and then add the
            # current instruction to the basic block being processed.
            lir_inst = LowLevelInstruction()

            if not self.set_instruction_info(lir_inst, inst):
                raise DisassemblerException(
                    "Unable to store information for instruction at 0x%08X" %
                    ea)

            current_basic_block.add_instruction(ea, lir_inst)

        return lir_function
