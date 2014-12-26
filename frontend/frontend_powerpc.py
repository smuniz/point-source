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

        if lir_inst.is_type(self.iset.PPC_addi):

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

                gep = self.mir_inst_builder.gep(
                    alloca,
                    [MiddleIrConstantInt32(0), MiddleIrConstantInt32(0)],
                    "szBuffer_0x%X" % address)

                gep.add_address(address)

                lir_inst.analyzed = True

                # Add newly created symbol to symbol table.
                self.current_symbols_table[address] = gep

            else:
                pass

        elif lir_inst.is_type(self.iset.PPC_clrlwi):
            pass

        elif lir_inst.is_type(self.iset.PPC_lbz):
            pass

        elif lir_inst.is_type(self.iset.PPC_li):
            self.current_symbols_table[address] = \
                MiddleIrConstantInt(MiddleIrTypeInt(32), lir_inst[1].value)

        elif lir_inst.is_type(self.iset.PPC_lis):
            pass

        elif lir_inst.is_type(self.iset.PPC_lwz):
            pass

        elif lir_inst.is_type(self.iset.PPC_mr):
            reg = lir_inst[1].value
            du_addr = self.lir_function.ud_chain[address].get(reg, None)

            if du_addr is None:
                raise FrontEndPowerPcException(
                    "DU chain for register %s at 0x%08X does not exists." % \
                    (self.iset.GPR_NAMES[reg], address))

            if du_addr in self.current_symbols_table:
                src = self.current_symbols_table[du_addr]

                # TODO / FIXME : Check if src is another MIR volatile
                # instruction.
                if isinstance(src, MiddleIrVolatileInstruction):
                    raise FrontEndPowerPcException(
                        "Chained MIR volatile instructions chaining is "
                        "unimplemented.")
                vol = MiddleIrVolatileInstruction(src)

                self.current_symbols_table[address] = vol
            else:
                raise FrontEndPowerPcException(
                    "No symbol found for DU chain address 0x%X at 0x%08X" % (
                    du_addr, address))

        elif lir_inst.is_type(self.iset.PPC_stb):
            pass

        elif lir_inst.is_type(self.iset.PPC_stw):

            # TODO / FIXME : Detect GPR3 as the first use of the first
            # argument.
            #arg = 
            if address not in self.current_symbols_table:
                return None

            stack_alloc = self.current_symbols_table[address]
            mir_inst = self.mir_inst_builder.store(arg, stack_alloc)

        elif lir_inst.is_type(self.iset.PPC_stwu):
            pass
            ##module = self.mir_module._llvm_getModule()

            #lhs = MiddleIrConstantInt32(lir_inst[0].value)

            #offset, reg = lir_inst[1].value
            #rhs_offset = MiddleIrConstantInt(offset)
            #rhs_reg = MiddleIrConstantInt(reg)

            #mir_inst = self.mir_inst_builder.add(rhs_offset, rhs_reg)
            ##print "--->", mir_inst._ptr
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
                pass
            else:
                #
                # Create a function call expression and add it to the IR
                #
                func_name = self.debugger.get_function_name(branch_address)

                mir_callee = MiddleIrFunction(func_name, self.mir_module)

                mir_callee.return_type = MiddleIrTypeVoid()
                #mir_callee.arguments = [MiddleIrTypeChar()] * 15
                mir_callee.arguments = MiddleIrTypePointer(MiddleIrTypeChar()),

                self.mir_module.add_function(mir_callee)

                # Assign a name to each argument of the function being called.
                for arg_index, arg in enumerate(mir_callee.arguments):
                    mir_callee.set_argument_name(0, "arg%s" % arg_index)

                # TODO : Obtain function arguments programatically.
                mir_callee_args = [self.current_symbols_table[0x40], ]

                mir_inst = self.mir_inst_builder.call(
                    mir_callee, mir_callee_args)

        elif lir_inst.is_type(self.iset.PPC_balways):
            #
            # Instruction : blr
            #
            if len(self.idiom_analyzer.return_registers) == 0:
                # Function does not return any value (prototype void).
                mir_inst = self.mir_inst_builder.ret(None)

            elif len(self.idiom_analyzer.return_registers) == 1:
                # Function returns a value (prototype of basic type).
                # Obtain return registers.
                ret_reg = self.idiom_analyzer.return_registers[0]

                op_address = self.lir_function.ud_chain[address][ret_reg]

                if not op_address in self.current_symbols_table:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % \
                        (op_address, lir_inst.address))

                ret_val = self.current_symbols_table[op_address]

                # In case we have a volatile instruction then obtain the real
                # instruction from it and move on.
                if isinstance(ret_val, MiddleIrVolatileInstruction):
                    ret_val = ret_val.llvm_instruction

                mir_inst = self.mir_inst_builder.ret(ret_val)

            else:  # 2 or more (types bigger than built-ins)
                raise FrontEndPowerPcException(
                    "Unsupported multiple return values %s" % \
                    self.idiom_analyzer.return_registers)

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
        mir_inst = None

        #lir_inst = UnknownExpression()
        #mir_inst.set(str(lir_inst))

        return mir_inst

    def is_call_instruction(self, lir_inst):
        """Determine if the specified instruction is a call instruction or
        not.

        """
        # TODO / FIXME : make this right.
        return bool(
            lir_inst.type == self.iset.PPC_b and \
            lir_inst._aux == 8 and \
            len(lir_inst) == 1 and \
            lir_inst[0].type in [O_NEAR, O_FAR])

    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        if not self.is_call_instruction(lir_inst):
            return None

        if len(lir_inst) == 1:
            return lir_inst[0].value

        return None

    def analyze_callee(self, callee_address):
        """Analyze the callee function by performing a live analysis on it."""
        lir_function = self.debugger.generate_lir(callee_address)
        #print lir_function
        return lir_function
