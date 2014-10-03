# 
# Copyright (c) 2013 Sebastian Muniz
#
# This code is part of point source decompiler
#

from traceback import format_exc

from idioms import IdiomAnalyzer, IdiomAnalyzerException

# Import MIR related modules
#from middleend.mir import *    # Not working anymore. Must import each module
                                # manually.
from middleend.mir_exception import MiddleIrException
from middleend.mir.mir_function import *


class PowerPc32GccIdiomAnalyzerException(IdiomAnalyzerException):
    """Generic exception for idioms analyzer on PowerPC architecture."""
    pass


class PowerPc32GccIdiomAnalyzer(IdiomAnalyzer):
    """PowerPC specific idioms analyzer support."""

    def __init__(self, debugger, lir_function, mir_module, mir_function,
        symbol_tables):
        """Initialize idiom analyzer for the PowerPC architecture."""
        IdiomAnalyzer.__init__(
            self, debugger, lir_function, mir_module, mir_function,
            symbol_tables)

        # Set default stack access style for PPC
        lir_function.add_stack_access_register(self.iset.SP)

    def perform_phase1_analysis(self):
        """Execute the basic idiom analysis on current function previous to MIR
        generation.

        """
        #print "Locating prologue."
        self.detect_prologue()

        #print "Locating epilogue."
        self.detect_epilogue()

        #print "Detecting parameters register."
        self.detect_parameter_registers()

        #print "Detecting return registers."
        self.detect_return_registers()

        #print "Detecting parameters copy."
        self.detect_parameters_copy()

        #print "Detecting 4 bytes load idioms."
        self.detect_load_word()

        #self.create_local_symbols()

    def create_local_symbols(self):
        """..."""
        for lir_basic_block in self.lir_function:
            for lir_instruction in lir_basic_block:

                mir_inst_builder = \
                    self.mir_function.get_instruction_builder_by_address(
                        lir_instruction.address, True)

                #mir_inst_builder.

    def perform_phase2_analysis(self):
        """Execute the basic idiom analysis on current function after to MIR
        generation.

        """
        #print "Detecting register variables."
        self.detect_register_variables()

        #print "Detecting function calling convention."
        self.detect_calling_convention()

        #print "Detecting compiler."
        self.detect_compiler()

        #print "Detecting unoptimized code idioms."
        self.detect_unoptimized_code_sequences()

        #print "Detecting 4 bytes load idioms."
        #self.detect_load_word()

    def detect_prologue(self):
        """Check wheater the function prologue is present or not."""
        #
        # Common prologue is as follows:
        #
        # mflr    %r0                    ; if not leaf proc, get ret address
        # stwu    %sp, -0x1A8(%sp)       ; allocate stack space
        # stmw    %r28, 0x1A8+var_10(%sp); store temp regs
        # stw     %r0, 0x1A8+arg_4(%sp)  ; store ret address
        #
        try:
            # Check the instructions from the first basic block
            # to find common function prologue
            bb = self.lir_function[0]

            # Check only in the first three instructions
            for inst in bb:
                # STEP 1.A
                #
                # Check if it modifies %sp and get the number of allocated
                # bytes.
                op0 = inst[0]
                op1 = inst[1]
                if inst.type == self.iset.PPC_stwu and \
                    op0.is_reg_n(self.iset.SP) and \
                    op1.is_displ and \
                    op1.value[0] == self.iset.SP:

                    #
                    # Mark instruction as already analyzed and as part of the 
                    # standard prologue instruction to avoid output representation.
                    #
                    self.mark_instruction_analyzed(inst)
                    self.mir_function.add_prologue_address(inst.address)
                    self.lir_function.add_prologue_address(inst.address)

                    # Add the stack size found.
                    stack_size = abs(self.get_signed_value( op1.value[1] ))
                    self.lir_function.stack_size = stack_size

                    break

            if self.lir_function.stack_size != 0:
                print "    Stack allocation found 0x%X (%d) bytes. Double check: " % \
                        (self.lir_function.stack_size,
                        self.lir_function.stack_size),

                # TODO: Check any difference with get_frame_size()
                frame_size = self.debugger.get_frame_size(inst.address)

                if self.lir_function.stack_size == frame_size:
                    print "OK"
                else:
                    print "INVALID (should be %d bytes)" % frame_size

            else:
                # This shouldn't happen so we abort in case it does but first
                # we run a check.
                print "[-] Stack allocation NOT found. Using debugger detection: ",

                # TODO / FIXME : Remove IDA specific function call.
                if GetFrameLvarSize(inst.address) == 0:
                    print "OK"
                else:
                    print "INVALID"

                raise PowerPc32GccIdiomAnalyzerException(
                    "Unable to determine stack size.")

            # STEP 1.B
            #
            # Obtain information about the method used to access
            # local variables.
            #
            # If we can't find a register used as a copy of sp, then
            # we asume IOS-style using SP like this:
            #
            #   add  rd, sp, imm
            #
            # TODO : why is there a slice in the enum below?
            for index, inst in enumerate(bb[1 : ], 1):
                # Start generating the high-level representation
                # of the current function to decompile the binary.
                # Indicate the prologue-related addresses to avoid
                # decompiling them.

                if inst.type == self.iset.PPC_mr and inst[1].is_reg_n(self.iset.SP):
                    # Seems that we've found an SP being moved to another
                    # register.
                    self.mir_function.add_prologue_address(inst.address)
                    self.lir_function.add_prologue_address(inst.address)
                    self.lir_function.add_stack_access_register(inst[0].value)

                    # Mark the instruction but before stop looking, confirm the
                    # finding by looking for that store operation on that
                    # register (backup).
                    #
                    # 018000BC stw     %r31, 28(%sp) ; Find this STW given
                    # 018000C0 mr      %r31, %sp     ;  this MR instruction.
                    #
                    # TODO: stack pointer definition !!!!!!!!!!!!!
                    self.mark_instruction_analyzed(inst)

                    for i in bb[index : 0 : -1]:  # walk backwards.

                        op0_value = i[0].value

                        if i.type in [self.iset.PPC_stw, self.iset.PPC_stwu] and \
                            op0_value in self.lir_function.stack_access_registers:

                            # Stack register backup operation found
                            self.mark_instruction_analyzed(i)
                            self.lir_function.add_prologue_address(i.address)
                    break

            # Output stack access information found.
            stack_access_registers = self.lir_function.stack_access_registers
            stack_access_registers = [
                self.iset.REGISTERS_NAMES[r] for r in stack_access_registers]

            if self.iset.SP in self.lir_function.stack_access_registers:
                stack_access_type = "    Stack accessed via stack-pointer: "
            else:
                stack_access_type = "    Stack accessed via frame-pointer: "

            print "%s %s" % (stack_access_type, ", ".join(stack_access_registers))

            # STEP 2
            # Another instruction should save %lr in case we aren't processing
            # a leaf procedure.
            # Look for the second isntruction of this sequence:
            #
            # mflr    %r0
            # ...
            # stw     %r0, 0xE0+arg
            for inst in bb:

                if inst.analyzed or not inst.type == self.iset.PPC_mflr:
                    continue

                lr_backup_reg = inst[0].value # dest reg for %lr
                lr_store_found = False              # flag
                self.mark_instruction_analyzed(inst)

                # Check only in the first n instructions
                for inst in bb:

                    if inst.analyzed:
                        continue

                    if inst.type == self.iset.PPC_stw and \
                        inst[0].is_reg_n(lr_backup_reg):

                        # Found LR store operation from previous move
                        self.mir_function.add_prologue_address(inst.address)
                        self.lir_function.add_prologue_address(inst.address)
                        self.mark_instruction_analyzed(inst)

                        lr_store_found = True
                        self.lir_function.leaf_procedure = False

                        break

                if not lr_store_found:
                    raise PowerPc32GccIdiomAnalyzerException(
                        "Could not locate link register backup instruction")

            if self.lir_function.leaf_procedure is True:
                print "    Current function is a leaf procedure."
            else:
                print "    Current function is NOT a leaf procedure."

        except MiddleIrException, err:
            print format_exc() + '\n'

            raise PowerPc32GccIdiomAnalyzerException(err)

    def __is_valid_return(self, inst):
        """Indicate if the specified instruction is a valid return instruction
        or not.

        """
        if inst.type == self.iset.PPC_balways:
            if not ((inst[0].type == self.iset.CRB and \
                inst[1].type == self.iset.SPR) or \
                (inst[0].type is self.iset.SPR)):
                return False
            return True
        return False

    def detect_epilogue(self):
        """Check wheater the function epilogue is present or not."""
        try:
            # Check the last basic block for the prescense of the epilogue.
            # TODO / FIXME : Check all the ending basic blocks, not just 1.
            bb = self.lir_function[-1]

            # STEP 1.A
            # Check the last instruction for a BLR opcode.
            inst = bb[-1]

            if inst.type == self.iset.PPC_balways:
                if not self.__is_valid_return(inst):
                    #
                    # In case that the branch instruction is unknown to us then
                    # we raise an exception becuase we don't know if it's a
                    # return, a goto of some kind or what it is at all.
                    #
                    # This shouldn't happen. In case it does please report.
                    raise PowerPc32GccIdiomAnalyzerException(
                        "Unknown branch instruction at 0x%X" % \
                        inst.address)

                # Do not mark the instruction as analyzed because
                # we'll use it to create the 'return' instruction
                # when translating to MIR.
                #self.mark_instruction_analyzed(inst)
                self.mir_function.add_epilogue_address(inst.address)
                self.lir_function.add_epilogue_address(inst.address)

                self.ret_to_caller = True
                print "    Function returns to caller."

                temp_lr_reg = -1

                # STEP 1.B
                #
                # If it's not a leaf procedure, detect lr restoration by 
                # locating the following instruction sequence.
                #
                # lwz     %r0, 4(%r11)
                # ...
                # mtlr    %r0
                if not self.lir_function.leaf_procedure and self.ret_to_caller:

                    # Check the last basic block except blr (last instruction).
                    # TODO / FIXME : Check all the ending basic blocks, not
                    # just 1.
                    for inst in bb[-2::-1]:

                        # Find mtlr instruction to locate the register used
                        if inst.type == self.iset.PPC_mtlr:
                            temp_lr_reg = inst[0].value

                            self.mark_instruction_analyzed(inst)
                            self.mir_function.add_epilogue_address(inst.address)
                            self.lir_function.add_epilogue_address(inst.address)

                        if inst.type == self.iset.PPC_lwz and \
                            inst[0].is_reg_n(temp_lr_reg):
                            self.mark_instruction_analyzed(inst)
                            self.mir_function.add_epilogue_address(inst.address)
                            self.lir_function.add_epilogue_address(inst.address)

                            print "    Link-register restoration found."

                            break

            else:
                # Indicate that the current function doesn't perform the common
                # return-to-caller operation.
                self.ret_to_caller = False
                print "    Warning: Function does NOT return to caller."

            # STEP 2
            #
            # Detect a stack restoration sequences like the following:
            #
            # // Case 1: Cisco IOS
            # // Case 2.A: Linux
            # // Case 2.B : PowerPC-ELF
            #
            if self.lir_function.stack_size > 0:

                # Check case 1 (Cisco IOS)
                #
                # addi    %sp, %sp, 0x1A8
                #
                prologue_block = list()

                for inst in bb[-1::-1]:
                    if inst.analyzed:
                        continue

                    if inst.type == self.iset.PPC_addi and inst[0].is_reg_n(self.iset.SP):

                        prologue_block.append(inst)

                        print "    Stack restoration style: IOS" 
                        self.stack_restore = "IOS"
                        
                        # Additional verification
                        if len(inst) == 3:
                            restore_size = self.get_signed_value(inst[2].value)
                            if self.lir_function.stack_size != restore_size:
                                print "[!] Restore value (%d bytes) does " \
                                    "NOT match stored value (%d bytes)" % \
                                    (restore_size, self.lir_function.stack_size)
                        
                        for inst in prologue_block:
                            self.mark_instruction_analyzed(inst)
                            self.mir_function.add_epilogue_address(inst.address)
                            self.lir_function.add_epilogue_address(inst.address)
                        return  # Don't keep checking

                # Check case 2.a (GCC w/Linux)
                #
                # Find the following epilogue sequence for stack
                # restoration:
                #
                # lwz     %r11, 0(%sp)
                # lwz     %r31, -4(%r11)
                # mr      %sp,  %r11  ; sp was first copied to r11 
                #
                restore_sp_reg = None
                restore_stages_found = 0

                prologue_block = list()

                for inst in bb[-1 : :-1]:

                    if inst.analyzed:
                        continue

                    elif inst.type == self.iset.PPC_mr and inst[0].is_reg_n(self.iset.SP):
                        prologue_block.append(inst)

                        restore_sp_reg = inst[1].value
                        restore_stages_found += 1

                    elif restore_sp_reg:

                        if inst.type == self.iset.PPC_lwz and \
                            inst[0].is_reg_n(restore_sp_reg):

                            # Found 2nd case of the stack restoration seq
                            prologue_block.append(inst)

                            restore_stages_found    += 1
                            self.stack_restore       = "Linux"

                            print "    Stack restoration style: linux"

                        elif inst.type == self.iset.PPC_lwz and \
                            inst[1].is_displ and \
                            inst[1].value[0] == restore_sp_reg and \
                            inst[0].value in self.lir_function.stack_access_registers:

                            prologue_block.append(inst)

                            restore_stages_found += 1
                            print "    Stack access register restoration found"

                if restore_stages_found == 3:
                    for inst in prologue_block:
                        self.mark_instruction_analyzed(inst)
                        self.mir_function.add_epilogue_address(inst.address)
                        self.lir_function.add_epilogue_address(inst.address)
                    return

                # Check case 2.b (GCC PowerPC-ELF)
                #
                # Find the following epilogue sequence for stack
                # restoration:
                #
                # addi    %r11, %r31, 0xE0
                # lwz     %r31, -4(%r11)
                # mr      %sp,  %r11  ; sp was first copied to r11 
                #
                restore_sp_reg = None
                restore_stages_found = 0

                prologue_block = list()

                for inst in bb[-1 : :-1]:
                    if inst.analyzed:
                        continue

                    if inst.type == self.iset.PPC_mr and inst[0].is_reg_n(self.iset.SP):
                        prologue_block.append(inst)

                        restore_sp_reg = inst[1].value
                        restore_stages_found += 1

                    elif restore_sp_reg:

                        if inst.type == self.iset.PPC_addi and \
                            inst[0].is_reg_n(restore_sp_reg) and \
                            inst[1].value in self.lir_function.stack_access_registers and \
                            inst[2].value == self.lir_function.stack_size:

                            # Found 2nd case of the stack restoration seq
                            prologue_block.append(inst)

                            restore_stages_found    += 1
                            self.stack_restore       = "Linux"

                            print "    Stack restoration style: GCC PowerPC-ELF"

                        elif inst.type == self.iset.PPC_lwz and \
                            inst[1].is_displ and \
                            inst[1].value[0] == restore_sp_reg and \
                            inst[0].value in self.lir_function.stack_access_registers:

                            prologue_block.append(inst)

                            restore_stages_found += 1
                            print "    Stack access register restoration found"

                if restore_stages_found == 3:
                    for inst in prologue_block:
                        self.mark_instruction_analyzed(inst)
                        self.mir_function.add_epilogue_address(inst.address)
                        self.lir_function.add_epilogue_address(inst.address)
                    return

            print "    Stack restoration analysis : INCOMPLETE"

        except MiddleIrException, err:
            print format_exc() + '\n'

            raise PowerPc32GccIdiomAnalyzerException(err)

        raise PowerPc32GccIdiomAnalyzerException(
            "Unable to locate epilogue.")

    def detect_register_variables(self):
        """Detect possible register variables in the prologue by detecting
        GPRs being stored in the stack.  We'll only check for non-volatile
        registers.

        """
        #
        # Bellow is the clasic non-volatile registers backup operation at the
        # first basic block:
        #
        # stmw %r27, 0x20+var_14(%sp)  ; store %r27 to %r31 simultaneously
        #
        # And next is the restore operation for those registers at the last
        # basic block:
        #
        # 80794E60 lmw %r28, 0x1A8+var_10(%sp)  ; restore %r27 to %r31 
        #                                       ; simultaneourly
        #
        try:
            # Iterate through every instruction in the first basic block
            for inst in self.lir_function[0]:

                # Avoid the instruction if it's part of a previously
                # detected idiom
                #print "inst at 0x%X...." % inst.address,
                if inst.analyzed:
                    #print "already analyzed"
                    continue

                # Find stores on stack for non-volatile registers between 
                # %13 and %31.
                # If a register between r0 and r12 is found as source operand
                # then discard the instruction.
                if inst[0].value < self.iset.GPR13:
                    #print "not non-vol reg"
                    continue

                #print "analyzing..."
                multiple_nv_reg = None

                if inst.type == self.iset.PPC_stw:
                    multiple_nv_reg = False

                elif inst.type == self.iset.PPC_stmw:
                    multiple_nv_reg = True

                if multiple_nv_reg is not None and \
                    inst[0].is_reg and \
                    inst[1].is_displ and \
                    inst[1].value[0] in \
                        self.lir_function.stack_access_registers:

                    # Store the registers numbers used as non-volatile.
                    if multiple_nv_reg is False:
                        self.nv_regs = range(inst[0].value, inst[0].value + 1)
                    else:
                        # TODO : This is probably WRONG !!!
                        self.nv_regs = [inst[0].value, self.iset.TOTAL_GPR]

                    print "--->", self.nv_regs

                    self.mark_instruction_analyzed(inst)
                    print "    Non-volatile registers detected:", self.nv_regs

                    #
                    # Now that non-volatile registers are known, find their
                    # restore location at the epilogue.
                    # 
                    bb = self.lir_function[-1]

                    for inst in bb[-1: 1 : -1]:
                        if inst.analyzed:
                            continue

                        if multiple_nv_reg:
                            restore_inst = self.iset.PPC_lmw
                        else:
                            restore_inst = self.iset.PPC_lwz

                        if inst.type == restore_inst and \
                            inst[0].is_reg_n(self.nv_regs[0]):
                            print "    Non-volatile registers restoration " \
                                    "found."
                            self.mark_instruction_analyzed(inst)

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    def detect_return_registers(self):
        """Detect registers used as retun values of the current function.

        """
        if not self.ret_to_caller:
            print "    Return registers not found : Function does not return"
            return

        #
        # Pre-requisites:
        #
        # interprocedural live register analysis has been performed.
        # intraprocedural reaching register definition has been performed.
        #
        blr = None

        for lir_basic_block in self.lir_function:
            for lir_inst in lir_basic_block:
                if self.__is_valid_return(lir_inst):
                    blr = lir_inst

        if not blr:
            raise PowerPc32GccIdiomAnalyzerException(
                "Not return instruction found ")

        #
        # Add empty UD and DU chains for this instruction given that it doesn't
        # contain any GPR so chains were never created in it.
        #
        self.lir_function.du_chain.setdefault(blr.address, dict())
        self.lir_function.ud_chain.setdefault(blr.address, dict())

        #
        # TODO / FIXME : We should perform this check with a call-flow graph
        # and make sure that the return register is indeed located before the
        # blr instruction.
        for lir_basic_block in reversed(self.lir_function):
            for lir_inst in reversed(lir_basic_block):
                if lir_inst.address in self.lir_function.du_chain:
                    # TODO / FIXME : We should check the the register is not
                    # used previous to the ret (and after the def).
                    # TODO / FIXME : We should have a list and remove the ones
                    # found.
                    for reg in self.iset.RETURN_REGISTERS:
                        reg_name = "r%d" % reg
                        if reg_name in self.lir_function.du_chain[lir_inst.address]:
                            # Update the list of return registers for further
                            # usage and then update the UD and DU chains of
                            # both the return instruction and the
                            # instruction(s) using the registers involved.
                            self.return_registers.append(reg)

                            self.lir_function.du_chain[lir_inst.address][reg_name].append(blr.address)

                            self.lir_function.ud_chain[blr.address][reg_name] = lir_inst.address

        print "    Return register(s) found : %s" % \
            ", ".join([self.iset.REGISTERS_NAMES[r] \
                for r in self.return_registers])

    def detect_parameter_registers(self):
        """Detect registers used for parameter passing to the current function.

        """
        try:
            # TODO / FIXME
            pass
        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)
            
    def detect_simple_parameter_registers(self):
        """Detect registers used for parameter passing to the current function.
        This is a simple (to say the least) version possile.

        """
        try:
            # Iterate through every instruction in the first basic block
            for inst in self.lir_function[0]:

                # Avoid the instruction if it's part of a previously
                # detected idiom
                if inst.analyzed:
                    continue

                # Look in the first basic block for an instruction
                # sequence like the following:
                #
                # .text:018000C4 stw     %r3, 8(%r31)
                # .text:018000C8 stw     %r4, 0xC(%r31)
                #
                if not inst.type == self.iset.PPC_stw:
                    continue

                # TODO: Do we need to check that destination is the stack?
                if inst[0].is_reg_n() and \
                    inst[0].value in self.iset.ARGUMENT_REGISTERS:

                    #self.param_regs[inst[1].value] = inst[0].value
                    self.mark_instruction_analyzed(inst)

                    print "    Parameter register detected: %s" % \
                            inst[0]

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    def detect_parameters_copy(self):
        """Check non-volatile registers used as a temporal function's
        parameters holder.

        """
        try:
            # Iterate through every instruction in the first basic block
            for inst in self.lir_function[0]:

                # Avoid the instruction if it's part of a previously
                # detected idiom
                if inst.analyzed:
                    continue

                # Look in the first basic block for an instruction
                # sequence like the following:
                #
                # mr      %r28, %r3
                # mr      %r30, $r4
                #
                if inst.type == self.iset.PPC_mr and \
                    inst[0].is_reg and \
                    inst[0].value in self.nv_regs and \
                    inst[1].is_reg and \
                    inst[1].value >= self.iset.GPR3 and \
                    inst[1].value <= self.iset.GPR10:

                    # TODO: check some of the function's reference to see if
                    #       any of those param registers is used immediately
                    #       before the function call... Just to make sure.

                    self.param_regs[inst[1].value] = inst[0].value
                    self.mark_instruction_analyzed(inst)

                    print "    Function's parameters copy register r%d->r%d detected" % \
                            (inst[1].value, inst[0].value)

        except MiddleIrException, err:
            # TODO: This kind of exception won't happen, right?
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    def detect_load_word(self):
        """
        Detect the following instruction sequence:

            lis     %r6, aSomeString@h # "some-string"
            addi    %r5, %r6, aSomeString@l # "some-string"

        and transform it into a statement like:

            %r5 = aSomeString # "some-string"

        """
        try:
            for bb in self.lir_function:

                for hi_inst in bb:
                    # TODO: add an offset parameter in case lis/addi are
                    #       not together (happens on fixed instruction
                    #       size architectures).
                    if hi_inst.analyzed:
                        continue

                    # The higher 16 bits are always set with a LIS instruciton.
                    if hi_inst.type == self.iset.PPC_lis:

                        # Get the LIS instruction position inside the current
                        # basic block.
                        hi_inst_idx = bb.get_instruction_index(hi_inst)

                        if not hi_inst_idx:
                            raise PowerPc32GccIdiomAnalyzerException(
                                "[-] Couldn't locate index for 0x%X:%s" \
                                % (hi_inst.address, hi_inst))

                        self.detect_load_word_lower(bb, hi_inst_idx)

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    def detect_load_word_lower(self, bb, hi_inst_idx):
        """Detects the lower 16 bit load operation to complete the word
        assignment into a processor register. The lower part instruction used
        could vary so we must perform a series of tests.

        """
        # Get the instruction referenced by at specified index.
        hi_inst = bb[hi_inst_idx]

        # Find the instruction that modifies the lower 16 bits.
        for lo_inst in bb[hi_inst_idx + 1 : ]:

            # Avoid the immediate (addi???) instruction because it could
            # reuse the registers like this:
            #
            # lis     %r3, ((sub_80028C04+0x10000)@h)
            # addi    %r3, %r3, -0x73FC # sub_80028C04
            #
            if bb[hi_inst_idx + 1] != lo_inst:

                # Stop looking if the register affecting the upper
                # part was redefined.

                # TODO: distinct between store and load operations.
                #if lo_inst.type == hi_inst.type and \
                if lo_inst[0].value == hi_inst[0].value:
                    #print "break at 0x%X" % lo_inst.address
                    break

            if ( lo_inst.type == self.iset.PPC_addi and \
                hi_inst[0].value == lo_inst[1].value ) \
                or \
                ( lo_inst.type == self.iset.PPC_lwz and \
                lo_inst[1].is_displ and \
                hi_inst[0].value == lo_inst[1].value[0] ):

                # Obtain the memory address referenced by the idiom.
                # TODO / FIXME: Remove IDA Pro specific API calls.
                raise PowerPc32GccIdiomAnalyzerException("kludge!!!!")
                address = 0x180037C  #FIXME: get_first_dref_from(hi_inst.address)
                idiom_type = "char*"  #idc_guess_type(address)

                #print "    0x%X (idx %2d) ---> 0x%X - %s" % \
                #        (lo_inst.address, hi_inst_idx, address, idiom_type)

                # Additional check to see if debugger recognized the
                # instruction sequence.
                #if get_first_dref_from(lo_inst.address) != address:
                    #print "[-] Unrecognized LOAD idiom at 0x%X" % \
                            #hi_inst.address
                    #continue

                # Check wheater the pointed address contains a string
                # or it's just a global variable.
                data  = self.get_string_by_address(address)

                if (idiom_type is not None and \
                    idiom_type.find("char") == -1) or \
                    data is None:
                    # Global variable reference
                    #
                    # TODO: Check if it's just an integer literal
                    # expression or a global variable reference.
                    #
                    #address  = (bb[i][1].value & 0xffff) << 16
                    #address += bb[i+1][2].value

                    pass
                    # TODO: Determine if the address belongs to a function.
                    #f = get_func(address)
                    #if f is not None and f.startEA == address:
                    #    expr = get_func_name(get_func(address).startEA)
                    #else:
                    #    expr = IntegerLiteralExpression(address)

                else:
                    #
                    # Add the newly detected string reference to the MIR
                    # module by creating an array of char (int 8) type and
                    # setting the string as its content.
                    #
                    buffer_size = len(data) + 1 # Add one for the NULL terminator.
                    array_type = MiddleIrTypeArray(MiddleIrTypeChar(), buffer_size)

                    # Create a global variable referencing the char array.
                    gvar_str = MiddleIrGlobalVariable(
                        array_type,
                        MiddleIrConstantStringZ(data),
                        "sz" + data.capitalize())

                    gvar_str.global_constant = True
                    gvar_str.alignment = 1

                    # Add the global variable to the current module.
                    self.mir_module.add_global_variable(gvar_str)

                    address = lo_inst.address

                    #
                    # Get an instruction builder and create a GEP instructino
                    # referencing the global variable.
                    #
                    mir_inst_builder = \
                        self.mir_function.get_instruction_builder_by_address(
                            address, True)

                    gep = mir_inst_builder.gep(
                        gvar_str,
                        [MiddleIrConstantInt32(0)] * 2,
                        "psz%s" % data.capitalize())

                    gep.add_address(address)

                    #
                    # Add newly created symbol to symbol table.
                    #
                    self.current_symbol_table[address] = gep

                    #
                    # Set MIR instruction address equivalent to the LIR
                    # instruction used to get it.
                    #
                    mir_basic_block = \
                        self.mir_function.get_basic_block_by_address(address)

                    mir_basic_block.add_instruction(gep)     # HACK / FIXME

                # Mark instructions as analyzed and remove them from
                # the list of remaining LIR instructions.
                self.mark_instruction_analyzed(hi_inst)
                self.mark_instruction_analyzed(lo_inst, remove=False)

        return True

    def detect_calling_convention(self):
        """Obtain the calling convention detected by the compiler."""
        # TODO: Detect calling convention.
        print "    Calling convention: %s" % \
            self.mir_function.calling_convention_name

        return True

    def detect_unoptimized_code_sequences(self):
        """When the source code is compiled without any optimization flag
        enabled, the code generated by the compiler might contain redundant
        instructions which were not changed/removed by the optimizer.

        The porpuse of this method is to locate such instructions sequence and
        handle them appropriately.

        """
        # Following is an example of unoptimized code:
        # 
        # 018000F4 lbz     %r0, 0(%r9)
        # 018000F8 clrlwi  %r0, %r0, 24
        #
        # The lbz instructions loads the 8 bits pointed by %r9 into %r0 and
        # sets the other bits to 0.
        # Next instruction (clrlwi) clears the upper 24 bits of %r0 and stores
        # it in %r0 again.
        #
        # The upper 24 bits were cleared by the lbz instruction already making
        # the second instruction unnecessary.
        #

        try:
            for bb in self.lir_function:
                for i in range(len(bb)-1):

                    # Ignore already processed instructions
                    if bb[i].analyzed:
                        continue

                    # Find lbz/clrlwi instruction sequence
                    if not (bb[i].type == self.iset.PPC_lbz and \
                        bb[i+1].type == self.iset.PPC_clrlwi):
                        continue

                    lbz = bb[i]
                    clrlwi = bb[i+1]

                    reg = lbz[0].value 

                    if clrlwi[0].is_reg_n(reg):
                        # Mark instructions as analyzed and remove them from
                        # the IR list.
                        self.mark_instruction_analyzed(bb[i], remove=False)
                        self.mark_instruction_analyzed(bb[i+1])

        except MiddleIrException, err:
            print format_exc() + '\n'
            raise PowerPc32GccIdiomAnalyzerException(err)

    def guess_compiler_type(self):
        """Try to determine the compiler."""
        # TODO / FIXME: Improve this "analisys".
        print "    Guessing compiler...",

        if self.stack_restore in ["IOS", "Linux"]:

            compiler_type = self.debugger.COMPILER_GNU
            self.set_compiler_type(compiler_type)

            return True

        return False
