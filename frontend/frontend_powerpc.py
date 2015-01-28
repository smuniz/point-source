# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_powerpc32_gcc
reload(idioms_powerpc32_gcc)
from idioms_powerpc32_gcc import PowerPc32GccIdiomAnalyzer

import actionplan
reload(actionplan)
from actionplan import Action, ActionPlan, ActionPlanException

#from frontend.lir.lir_operand import *
from lir.lir_operand import *

# Import MIR related modules
#from middleend.mir import *    # Not working anymore. Must import each module
                                # manually.
from middleend.mir.mir_constants import *
from middleend.mir.mir_instruction import *
from middleend.mir.mir_basicblock import *
from middleend.mir.mir_function import *

class FrontEndPowerPcException(Exception):
    """Front-end exception for PowerPC architecture."""
    pass


class FrontEndPowerPc(FrontEnd):
    """Front-end support for the PowerPC architecture."""

    TARGET_ARCH = "PowerPC"

    def __init__(self, debugger):
        """Perform PowerPC front-end instance initialization."""
        super(FrontEndPowerPc, self).__init__(
            PowerPc32GccIdiomAnalyzer, debugger)

    def calculate_stack_buffer_limits(self):
        """Determine the size of the stack with taking into account
        architecture specific values, only variables.
        
        """
        # TODO: Make this more accurate
        return self.lir_function.stack_size - self.stack_lower_limit

    @property
    def stack_lower_limit(self):
        """Return the minimal size that the stack can hold."""
        return 0x10

    def on_assignment(self, lir_inst):
        """Handle Low level IR assignment instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        mir_inst = None

        address = lir_inst.address

        if lir_inst.is_type(self.iset.PPC_add):
            # Instruction : add

            op0 = lir_inst[0]
            op1 = lir_inst[1]
            op2 = lir_inst[2]

            if op1.value in \
                self.lir_function.stack_access_registers:

                raise FrontEndPowerPc(
                    "PPC_add with stack variables is unimplemented")
#                # TODO/FIXME : This won't work for multiple buffers in stack.
#
#                # Add the newly detected stack buffer to the MIR module.
#                array_size = self.calculate_stack_buffer_limits() - \
#                    op2.value
#
#                array_type = MiddleIrTypeArray(MiddleIrTypeChar(), array_size)
#
#                alloca = self.mir_inst_builder.alloca(array_type, "szBuffer")
#
#                alloca.add_address(address)
#
#                name = "szBuffer_0x%X" % address
#
#                mir_inst = self.mir_inst_builder.gep(
#                    alloca,
#                    [MiddleIrConstantInt32(0), MiddleIrConstantInt32(0)],
#                    name)
            else:
                # Not a stack access register.
                op_address_1 = self.lir_function.ud_chain[address][op1.value]

                if not op_address_1 in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % (
                        op_address_1, lir_inst.address))

                op_address_2 = self.lir_function.ud_chain[address][op2.value]

                if not op_address_2 in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % (
                        op_address_1, lir_inst.address))

                name = "BLAAAA"

                mir_inst = self.mir_inst_builder.add(
                    self.current_symbols_table.symbols[op_address_1].item,
                    self.current_symbols_table.symbols[op_address_2].item,
                    name)

            mir_inst.add_address(address)

            lir_inst.analyzed = True
            #mir_inst.is_used = True

            # Add newly created symbol to symbol table.
            self.current_symbols_table.add_symbol(
                address, name, None, None, mir_inst)

        elif lir_inst.is_type(self.iset.PPC_addi):
            # Instruction : Add inmediate

            op0 = lir_inst[0]
            op1 = lir_inst[1]
            op2 = lir_inst[2]

            if op1.value in \
                self.lir_function.stack_access_registers:

                # TODO/FIXME : This won't work for multiple buffers in stack.

                # Add the newly detected stack buffer to the MIR module.
                array_size = self.calculate_stack_buffer_limits() - \
                    op2.value

                array_type = MiddleIrTypeArray(MiddleIrTypeChar(), array_size)

                alloca = self.mir_inst_builder.alloca(array_type, "szBuffer")

                alloca.add_address(address)

                name = "szBuffer_0x%X" % address

                mir_inst = self.mir_inst_builder.gep(
                    alloca,
                    [MiddleIrConstantInt32(0), MiddleIrConstantInt32(0)],
                    name)
            else:
                # Not a stack access register.
                op_address = self.lir_function.ud_chain[address][op1.value]

                if not op_address in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found for op n.%d at 0x%X for instruction at 0x%X" % (
                        1, op_address, lir_inst.address))

                name = "BLAAAA"

                mir_inst = self.mir_inst_builder.add(
                    self.current_symbols_table.symbols[op_address].item,
                    MiddleIrConstantInt(MiddleIrTypeInt(32), op2.value),
                    name)

            mir_inst.add_address(address)

            lir_inst.analyzed = True
            #mir_inst.is_used = True

            # Add newly created symbol to symbol table.
            self.current_symbols_table.add_symbol(
                address, name, None, None, mir_inst)

        elif lir_inst.is_type(self.iset.PPC_clrlwi):
            # Instruction : clear left with inmediate
            pass

        elif lir_inst.is_type(self.iset.PPC_cmpwi):
            # Instruction : compare word inmediate
            pass

        elif lir_inst.is_type(self.iset.PPC_lbz):
            # Instruction : load byte and zero
            pass

        elif lir_inst.is_type(self.iset.PPC_li):
            # Instruction : load inmediate

            # Add symbol to the symbols table.
            self.current_symbols_table.add_symbol(
                address, None, None, None,
                MiddleIrConstantInt(MiddleIrTypeInt(32), lir_inst[1].value))

        elif lir_inst.is_type(self.iset.PPC_lis):
            pass

        elif lir_inst.is_type(self.iset.PPC_lwz):
            # Instruction : load word and zero

            # Determine if destination is the stack or any other location.
            is_stack_src = lir_inst[1].value[0] in \
                self.lir_function.stack_access_registers

            if is_stack_src:
                # Seems like the destination register used as base is a stack
                # (or copy of) access register so we'll go this way.
                src_offset = lir_inst[1].value[1]  # Get second element of the
                                                    # tuple.

                # We're about to store a value in the stack so we first check
                # if the stack variable as been previously created and do it in
                # case it didn't.
                if src_offset in self.current_symbols_table.variables:
                    mir_var = \
                        self.current_symbols_table.variables[src_offset].item
                else:
                    raise FrontEndPowerPcException(
                        "Accesing stack without initialization at 0x%08X" % \
                        lir_inst.address)

                mir_inst = self.mir_inst_builder.load(mir_var)

                # Add symbol to the symbols table.
                self.current_symbols_table.add_symbol(
                    address, None, None, None, mir_inst)

            else:
                # A memory area not being the stack is being accessed.
                raise FrontEndPowerPcException(
                    "PPC_lwz on non-stack is unimplemented")

        elif lir_inst.is_type(self.iset.PPC_mr):
            reg = lir_inst[1].value
            du_addr = self.lir_function.ud_chain[address].get(reg, None)

            if du_addr is None:
                raise FrontEndPowerPcException(
                    "DU chain for register %s at 0x%08X does not exists." % \
                    (self.iset.GPR_NAMES[reg], address))

            if du_addr in self.current_symbols_table.symbols:
                src = self.current_symbols_table.symbols[du_addr].item
            elif du_addr in self.current_symbols_table.variables:
                src = self.current_symbols_table.variables[du_addr].item
            else:
                #print self.current_symbols_table
                raise FrontEndPowerPcException(
                    "No symbol found for DU chain (reg %s) at address "
                    "0x%08X referenced by 0x%08X" % (
                    self.iset.GPR_NAMES[reg], du_addr, address))

            # Add symbol to the symbols table.
            self.current_symbols_table.add_symbol(
                address, None, None, None, src)

        elif lir_inst.is_type(self.iset.PPC_stb):
            # Instruction : store byte
            pass

        elif lir_inst.is_type(self.iset.PPC_stw):
            # Instruction : store word

            # Determine if destination is the stack or any other location.
            if self._is_stack_destination(lir_inst):
                # Seems like the destination register used as base is a stack
                # (or copy of) access register so we'll go this way.
                dest_offset = lir_inst[1].value[1]  # Get second element of the
                                                    # tuple.

                # We're about to store a value in the stack so we first check
                # if the stack variable as been previously created and do it in
                # case it didn't.
                if dest_offset in self.current_symbols_table.variables:
                    mir_var = \
                        self.current_symbols_table.variables[dest_offset].item
                else:
                    mir_var = self._create_local_variable(dest_offset)

                # Use the newly created MIR viariable in the store
                # operation to fully represent the instruction.
                rs_reg = lir_inst[0].value

                # Determine if the source register is anything else besides a
                # parameter register.
                if lir_inst[0].value in [3, 4, 5, 6, 7]: # TODO / FIXME : Remove hardcoded value
                #if True:#self.is_parameter_register(lir_inst, 0):
                    param_idx = self.iset.ARGUMENT_REGISTERS.index(rs_reg)

                    try:
                        rs = self.mir_function.arguments[param_idx]
                    except IndexError, err:
                        raise FrontEndPowerPcException(
                            "Unable to locate rS parameter symbol.")

                    # TODO / FIXME : We should use the symbols table, right?
                    #rs = self.current_symbols_table.parameters.get(param_idx, None)

                    #print "=-=-=-> rS %s - rD %s" % (type(rs), mir_var)
                else:
                    sym_addr = self.lir_function.ud_chain[address][rs_reg]

                    rs = self.current_symbols_table.symbols[sym_addr].item
                    #raise Exception("STW non-register parameters.")

                mir_inst = self.mir_inst_builder.store(rs, mir_var)
                mir_inst.is_used = True

                # Add newly created symbol to symbol table.
                self.current_symbols_table.add_symbol(
                    address, None, None, None, mir_inst)

            else:
                # A memory area not being the stack is being accessed.
                raise FrontEndPowerPcException(
                    "PPC_stw on non-stack is unimplemented")

        #elif lir_inst.is_type(self.iset.PPC_stwu):
        #    pass
            ##module = self.mir_module._llvm_getModule()

            #lhs = MiddleIrConstantInt32(lir_inst[0].value)

            #offset, reg = lir_inst[1].value
            #rhs_offset = MiddleIrConstantInt(offset)
            #rhs_reg = MiddleIrConstantInt(reg)

            #mir_inst = self.mir_inst_builder.add(rhs_offset, rhs_reg)
            ##print "--->", mir_inst._ptr

        elif lir_inst.is_type(self.iset.PPC_subf):
            # Instruction : substract from

            op0 = lir_inst[0]
            op1 = lir_inst[1]
            op2 = lir_inst[2]

            if op1.value in \
                self.lir_function.stack_access_registers:

                raise FrontEndPowerPc(
                    "PPC_subf with stack variables is unimplemented")
#                # TODO/FIXME : This won't work for multiple buffers in stack.
#
#                # Add the newly detected stack buffer to the MIR module.
#                array_size = self.calculate_stack_buffer_limits() - \
#                    op2.value
#
#                array_type = MiddleIrTypeArray(MiddleIrTypeChar(), array_size)
#
#                alloca = self.mir_inst_builder.alloca(array_type, "szBuffer")
#
#                alloca.add_address(address)
#
#                name = "szBuffer_0x%X" % address
#
#                mir_inst = self.mir_inst_builder.gep(
#                    alloca,
#                    [MiddleIrConstantInt32(0), MiddleIrConstantInt32(0)],
#                    name)
            else:
                # Not a stack access register.
                op_address_1 = self.lir_function.ud_chain[address][op1.value]

                if not op_address_1 in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % (
                        op_address_1, lir_inst.address))

                op_address_2 = self.lir_function.ud_chain[address][op2.value]

                if not op_address_2 in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % (
                        op_address_1, lir_inst.address))

                name = "BLAAAA"

                mir_inst = self.mir_inst_builder.sub(
                    self.current_symbols_table.symbols[op_address_1].item,
                    self.current_symbols_table.symbols[op_address_2].item,
                    name)

            mir_inst.add_address(address)

            lir_inst.analyzed = True
            #mir_inst.is_used = True

            # Add newly created symbol to symbol table.
            self.current_symbols_table.add_symbol(
                address, name, None, None, mir_inst)

        else:
            raise FrontEndPowerPcException(
                "Unable to transform LIR instruction (%s) at 0x%X "
                "on '%s' group." % (
                    lir_inst, lir_inst.address, lir_inst.group_name))

        return mir_inst

    def on_unconditional_branch(self, lir_inst):
        """Handle Low level IR unconditional branch instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        mir_inst = None

        address = lir_inst.address

        if lir_inst.is_type(self.iset.PPC_b):
            #
            # Instruction : b
            #

            # Get the operand value and treat it like an address to 
            # check if it belongs to the current function's range.
            #
            # This way we detect if it belongs to a function call or 
            # a GOTO statement.
            branch_address = lir_inst[0].value

            # Check if the unconditional jump is a GOTO to an offset into the
            # current function or a call to a another function.
            # Determine that checking the jump destination address against the
            # address range of the current function.
            # TODO : The right way to do this should be to check if LR is set.
            if self.lir_function.has_address(branch_address):
                # TODO: Label statement might not have been created so
                #       we have to do a second pass later when all the
                #       statements and expressions are in place.
                #lir_inst = GotoStatement()

                # Get local label statement
                #mir_inst.set(branch_address)
                raise FrontEndPowerPcException("GOTO statements unimplemented")
            else:
                #
                # Create a function call expression and add it to the IR.
                #
                # Make sure that they've already analyzed the callee function
                # and we have it in the cache.
                lir_callee = self.lir_functions_cache.get(
                    branch_address, None)

                if lir_callee is None:
                    raise FrontEndPowerPcException(
                        "Unable to locate callee function at 0x%08X" % \
                        branch_address)

                mir_callee = MiddleIrFunction.get(self.mir_module, lir_callee.name)

                if mir_callee is None:
                    raise FrontEndPowerPcException(
                        "Unable to get supposedly existing MIR function" \
                        " '%s' at 0x%08X" % (
                        lir_callee.name, lir_callee.start_address))

                du_chain_regs = lir_callee.du_chain[lir_callee.start_address].keys()

                self.lir_function.update_chains(
                    du_chain_regs, lir_inst.address, forward=False)

                # TODO : Enhance this code.
                # Process every parameter for the callee and add it to a list
                # of arguments to pass from the caller.
                mir_callee_args = list()

                for arg_idx, (reg_arg, reg_arg_address) in \
                    enumerate(self.lir_function.ud_chain[address].iteritems()):
                    #print "arg %d (0x%08X) reg %d" % (
                    #    arg_idx, reg_arg_address, reg_arg)
                    
                    mir_callee_args.append(
                        self.current_symbols_table.symbols[reg_arg_address].item
                        )

                print "[+] About to create call with %d parameters" % \
                    len(lir_callee.param_regs)

                # Display arguments matching (debugging purposes).
                for idx, (param_reg, mir_func_arg) in lir_callee.param_regs.iteritems():
                    print "    Param %2d : %r -> %r" % (
                        idx, self._class_name(mir_callee_args[idx]), 
                        self._class_name(mir_func_arg))

                    # Perform any cast/convertion if appropriate.
                    convertion_routine = self._argument_requires_convertion(
                        mir_callee_args[idx], mir_func_arg)
                    if convertion_routine is not None:
                        print "    Argument %d required convertion" % arg_idx
                        new_mir_inst = convertion_routine(self, mir_callee_args[idx], mir_func_arg)
                        if new_mir_inst is None:
                            raise FrontEndPowerPcException(
                                "Unable to perform argument %d conversion: "
                                "%s -> %s." % (
                                    idx,
                                    self._class_name(mir_callee_args[idx]), 
                                    self._class_name(mir_func_arg)))
                        mir_callee_args[idx] = new_mir_inst

                mir_inst = self.mir_inst_builder.call(
                    mir_callee, mir_callee_args)
                mir_inst.is_used = True

        elif lir_inst.is_type(self.iset.PPC_balways):
            #
            # Instruction : blr
            #
            if len(self.lir_function.return_registers) == 0:
                # Function does not return any value (prototype void).
                mir_inst = self.mir_inst_builder.ret(None)

            elif len(self.lir_function.return_registers) == 1:
                # Function returns a value (prototype of basic type).
                # Obtain return registers.
                ret_reg = self.lir_function.return_registers[0]

                op_address = self.lir_function.ud_chain[address][ret_reg]

                if not op_address in self.current_symbols_table.symbols:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % \
                        (op_address, lir_inst.address))

                mir_inst = self.mir_inst_builder.ret(
                    self.current_symbols_table.symbols[op_address].item)

            else:  # 2 or more (types bigger than built-ins)
                raise FrontEndPowerPcException(
                    "Unsupported multiple return values %s" % \
                    self.lir_function.return_registers)

            mir_inst.is_used = True

        else:
            raise FrontEndPowerPcException(
                "Unable to transform LIR instruction (%s) at 0x%X "
                "on '%s' group." % (
                    lir_inst, lir_inst.address, lir_inst.group_name))

        return mir_inst

    def on_conditional_branch(self, lir_inst):
        """Handle Low level IR conditional branch instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        mir_inst = None

        if lir_inst.is_type(self.iset.PPC_beq):
            pass

        else:
            raise FrontEndPowerPcException(
                "Unable to transform LIR instruction (%s) at 0x%X "
                "on '%s' group." % (
                    lir_inst, lir_inst.address, lir_inst.group_name))

        return mir_inst

    def on_unknown(self, lir_inst):
        """Handle unknown Low level IR instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        return None

    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        if not self.idiom_analyzer.is_call_instruction(lir_inst):
            return None

        if len(lir_inst) == 1:
            return lir_inst[0].value

        return None

    def analyze_callee(self, callee_address):
        """Analyze the callee function by performing a live analysis on it."""
        lir_function = self.debugger.generate_lir(callee_address)
        #print lir_function
        return lir_function

    def _is_stack_destination(self, lir_inst):
        """Check that destination of the operation is the stack."""
        # Is there any PPC instruction whose source is not first operand
        # and destination are the others and can store values in the stack?
        # Not that I know so this should work.
        #if lir_inst[0].is_reg_n(self.iset.ARGUMENT_REGISTERS) and \
        if lir_inst[1].is_displ_n(
            self.lir_function.stack_access_registers):
            return True
        return False

