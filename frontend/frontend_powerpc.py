# 
# Copyright (c) 2013 Sebastian Muniz
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
                self.current_symbol_table[address] = gep

            else:
                pass

        elif lir_inst.is_type(self.iset.PPC_clrlwi):
            pass

        elif lir_inst.is_type(self.iset.PPC_lbz):
            pass

        elif lir_inst.is_type(self.iset.PPC_li):
            self.current_symbol_table[address] = \
                MiddleIrConstantInt32(lir_inst[1].value)

        elif lir_inst.is_type(self.iset.PPC_lis):
            pass

        elif lir_inst.is_type(self.iset.PPC_lwz):
            print "PPC_lwz"
            pass

        elif lir_inst.is_type(self.iset.PPC_mr):
            reg = lir_inst[1].value
            du_addr = self.lir_function.ud_chain[address].get(reg, None)

            if du_addr is not None:
                src = self.current_symbol_table[du_addr]

                # TODO / FIXME : Check if src is another MIR volatile
                # instruction.
                vol = MiddleIrVolatileInstruction(src)

                self.current_symbol_table[address] = vol

        elif lir_inst.is_type(self.iset.PPC_stb):
            pass

        elif lir_inst.is_type(self.iset.PPC_stw):

            # TODO / FIXME : Detect GPR3 as the first use of the first
            # parameter.
            #arg = 
            if address not in self.current_symbol_table:
                return None

            stack_alloc = self.current_symbol_table[address]
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

                # TODO : Obtain function parameters programatically.
                called_mir_func_args = [
                    #self.current_symbol_table[self.        symbol_table.keys()[0]],
                    #self.current_symbol_table[self.        symbol_table.keys()[1]]
                    ]

                called_mir_func = MiddleIrFunction(func_name, self.mir_module)

                typtr = MiddleIrTypePointer

                called_mir_func.return_type = MiddleIrTypeVoid()
                called_mir_func.parameters = [
                    typtr(MiddleIrTypeChar()), typtr(MiddleIrTypeChar()) ]

                self.mir_module.add_function(called_mir_func)

                ########################
                called_mir_basic_block = MiddleIrBasicBlock()
                called_mir_func.add_basic_block(called_mir_basic_block)

                called_mir_builder = MiddleIrInstructionBuilder(called_mir_basic_block)

                called_mir_basic_block.instruction_builder = called_mir_builder
                called_mir_basic_block.start_address = branch_address
                called_mir_basic_block.end_address = branch_address + 0x10

                ret = called_mir_builder.ret()
                ret.add_address(branch_address)

                called_mir_basic_block.add_instruction(ret)
                ########################

                called_mir_func.set_argument_name(0, "pszDest")
                called_mir_func.set_argument_name(1, "pszSource")

                mir_inst = self.mir_inst_builder.call(
                    called_mir_func, called_mir_func_args)

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

                if not op_address in self.current_symbol_table:
                    raise FrontEndPowerPcException(
                        "No symbol found at 0x%X for instruction at 0x%X" % \
                        (op_address, lir_inst.address))

                ret_val = self.current_symbol_table[op_address]

                # In case we have a volatile instruction then obtain the real
                # instruction from it and move on.
                if isinstance(ret_val, MiddleIrVolatileInstruction):
                    ret_val = ret_val.llvm_instruction

                mir_inst = self.mir_inst_builder.ret(ret_val)

            else:  # 2 or more.
                # TODO / FIXME
                raise FrontEndPowerPcException(
                    "Unsupported multiple return values %s" % \
                    self.idiom_analyzer.return_registers)

        return mir_inst

    def on_conditional_branch(self, lir_inst):
        """Handle Low level IR conditional branch instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        mir_inst = None

        if lir_inst.is_type(self.iset.PPC_beq):
            pass

        return mir_inst

    def on_unknown(self, lir_inst):
        """Handle unknown Low level IR instructions.

        :param lir_inst: LIR instruction to convert into MIR instruction.
        """
        mir_inst = None

        #lir_inst = UnknownExpression()
        #mir_inst.set(str(lir_inst))

        return mir_inst
