# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from copy import deepcopy
from traceback import format_exc

from middleend.mir.mir_function import *
from middleend.mir.mir_constants import *
from middleend.mir.mir_type import *
from middleend.mir.mir_instruction import *

import cbackend.hir.area
reload(cbackend.hir.area)
from cbackend.hir.area import Area

#import cbackend.hir.graph
#reload(cbackend.hir.graph)
#from cbackend.hir.graph import Graph

import cbackend.hir.operators
reload(cbackend.hir.operators)
from cbackend.hir.operators import *

import cbackend.hir.expressions
reload(cbackend.hir.expressions)
from cbackend.hir.expressions import *

import cbackend.hir.statements
reload(cbackend.hir.statements)
from cbackend.hir.statements import *

import cbackend.hir.function
reload(cbackend.hir.function)
from cbackend.hir.function import Function, FunctionException

import cbackend.hir_text_output
reload(cbackend.hir_text_output)
from cbackend.hir_text_output import HirTextOutput

__all__ = ["CBackEnd", "CBackEndException"]

MIR_TYPE_TO_HIR_STRING = {
    MiddleIrTypeChar            : "char",
    MiddleIrTypeInt             : "int",
    MiddleIrTypeFloat           : "float",
    MiddleIrTypeDouble          : "double",
    #MiddleIrTypeX86Fp80         : "t_float_80",
    #MiddleIrTypePpcFp128        : "t_ppc_float_128",
    #MiddleIrTypeFp128           : "t_float_128",
    MiddleIrTypeFunction        : "t_func_",
    #MiddleIrTypeOpaque          : "t_opaque_",
    MiddleIrTypeStruct          : "struct",
    #MiddleIrTypePackedStruct    : "struct",
    MiddleIrTypeArray           : "[]",
    MiddleIrTypePointer         : "*",
    #MiddleIrTypeVector          : "[]",
    #MiddleIrTypeLabel           : "label_",
    MiddleIrTypeVoid            : "void",
    }


class CBackEndException(Exception):
    pass


class CBackEnd(object):
    """Given the IR code, transform it into a C/C++ readable code, display it
    appropiately and  perform callbacks if applicable.
    
    """

    DEFAULT_LABEL_INDENT = 4

    def __init__(self, mir=None):
        """Initialize instance."""
        # Initialize MIR storage with the specified module.
        self.mir = mir

        # Initialize HIR storage.
        self.hir_function = None

        self.function_name = None
        self.function_address = None

        self.label_indent = self.DEFAULT_LABEL_INDENT

        # Development flags
        self.debug_inst_info = True

    @property
    def symbols_manager(self):
        """Return the symbols manager instance for the current application."""
        return self._symbols_manager

    @symbols_manager.setter
    def symbols_manager(self, symbols_manager):
        """Store the symbols manager instance for the current application."""
        self._symbols_manager = symbols_manager

    @property
    def mir(self):
        """Return the intermediate language representation of the entire
        module.
        
        """
        return self._mir

    @mir.setter
    def mir(self, mir):
        """Store the intermediate language representation of the module."""
        self._mir = mir

    @property
    def hir_function(self):
        """Return the high level IR."""
        return self._hir

    @hir_function.setter
    def hir_function(self, hir):
        """Store the high level IR for further usage."""
        self._hir = hir

    @property
    def label_indent(self):
        """Return the indentation for labels."""
        return self._label_indent

    @label_indent.setter
    def label_indent(self, indent):
        """Store the indentation for Labels."""
        self._label_indent = indent

    @property
    def function_name(self):
        """Return the name of the function being decompiled."""
        return self._function_name

    @function_name.setter
    def function_name(self, name):
        """Store the name of the function being decompiled."""
        self._function_name = name

    @property
    def function_address(self):
        """Return the address of the function being decompiled."""
        return self._function_address

    @function_address.setter
    def function_address(self, address):
        """Store the address of the function being decompiled."""
        self._function_address = address

    def generate_hir(self):
        """
        Convert all the function's instructions represented by the MIR to a
        higher IR called HIR (high-end Intermediate Representation) as an
        initial step.

        Further analysis should discard other constructions and as a result a
        more compact and accurate IR will be obtained as a final phase from the
        Back-end.

        """
        try:
            # Obtain the current being decompiled to start the final
            # decompilation process.
            self.mir_function = self.mir.get_function_by_address(
                self.function_address) 

            # self.hir_function must contain a global scope and the newly created
            # function in it.
            self.hir_function = Function(self)
            self.hir_function.symbols_manager = self.symbols_manager

            # Pass addresses for instruction tracking purposes.
            for address in self.mir_function.prologue_addresses:
                self.hir_function.add_prologue_address(address)

            for address in self.mir_function.epilogue_addresses:
                self.hir_function.add_epilogue_address(address)

            #
            # Get all the information for the function declaration. This
            # includes return type, function name, all the parameters with
            # its respective types and optionally the calling convention.
            #
            self.hir_function.name = self.mir_function.name

            self.hir_function.return_type = \
                self.map_mir_type_to_hir_repr(self.mir_function.return_type)

            self.hir_function.parameters = self.mir_function.arguments

            #
            # Iterate through every basic block represented in the MIR and
            # create its HIR equivalent (block statement) with the appropriate
            # statements and expressions inside.
            #
            self.hir_block_stmt = CompoundStatement()
            self.hir_function.add_block(self.hir_block_stmt)

            # Store the current symbol table to use.
            self.current_symbols_table = \
                self.symbols_manager.symbols(self.function_address)

            for bb_idx, mir_basic_block in enumerate(self.mir_function):
                #print "-> Basic block %d (%s):%s" % (
                #    bb_idx, mir_basic_block.label, mir_basic_block)

                self.hir_block_stmt.label = mir_basic_block.label

                for mir_inst in mir_basic_block:
                    # Make sure that the MIR object is in fact a MIR
                    # instruction. We've allocated other MIR objects that are
                    # not instructions, i.e. MiddleIrConstantInt, and hence we
                    # must make sure what it is before proceeding.
                    if not isinstance(mir_inst, MiddleIrInstruction):
                        continue

                    #
                    # This step is very important.
                    # This is where most of the MIR instruction are translated
                    # to its HIR equivalents for further usage.
                    #
                    hir_stmt = self.transform_mir_to_hir(mir_inst)

                    #mir_address = mir_inst.address
                    #hir_is_used = self.current_symbols_table.
                    if hir_stmt is not None and \
                        mir_inst.is_used is True:
                        # Now the newly created instruction is stored in a basic
                        # block, whose purpose is to represent a group of
                        # instructions altogether.
                        self.hir_block_stmt.add_statement(hir_stmt)

                        # Copy all graph information from low-level representation to the
                        # intermediate-level language.
                        #self.__propagate_graph_information()

        except Exception, err:
            # TODO add a more accurate exception handler.
            print format_exc()

            raise CBackEndException(
                "High level IR code generation failed : %s" % err)

    def transform_mir_to_hir(self, mir_inst):
        """Get the corresponding HIR statement according to the MIR
        instruction.

        This is language-specific.

        """
        #
        # First we check if the instruction at the current address was
        # previously analyzed and marked for conversion by the idiom analyzer.
        #
        #if self.action_plan.has_plan_for_address(mir_inst.address):
        #    pass

        #
        # Dispatch the current MIR instruction to be appropriate type
        # conversion routine to be transformed into its equivalent HIR
        # statement(s).
        #
        hir_stmt = None
        group_name = mir_inst.group_name

        print "=" * 30
        if mir_inst.group is TERMINATOR_GROUP:
            hir_stmt = self.on_terminator(mir_inst)

        elif mir_inst.group is MEMORY_ACCESS_GROUP:
            hir_stmt = self.on_memory_access(mir_inst)

        elif mir_inst.group is BINARY_OP_GROUP:
            hir_stmt = self.on_binary(mir_inst)

        elif mir_inst.group is CONVERTION_GROUP:
            hir_stmt = self.on_conversion(mir_inst)

        elif mir_inst.group is OTHER_GROUP:
            hir_stmt = self.on_other(mir_inst)

        # Check if the translation mechanism worked. In case it didn't we;ll
        # raise an exception and notify the user about the offending
        # instruction.
        #
        # This should be submitted for analysis in case that the user agrees.
        #
        if not hir_stmt:
            raise CBackEndException(
                "Empty instruction (%s) at %s on '%s' group." % (
                    str(mir_inst).strip(),
                    ", ".join(["0x%08x" % a for a in mir_inst.addresses]),
                    group_name))

        # Set HIR statement address equal to the MIR instruction used
        # to get it.
        #
        # Store the instruction address for debugging purposes.
        hir_stmt.addresses = deepcopy(mir_inst.addresses)
        print "%s HIR STMT addresses ----->" % ",".join(["0x%x" % x for x in mir_inst.addresses]), 
        print ",".join(["0x%x" % x for x in hir_stmt.addresses])

        self.__display_instruction_information(mir_inst, group_name)

        return hir_stmt

    def on_terminator(self, mir_inst):
        """Process a MIR terminator instruction."""
        addresses = mir_inst.addresses
        print "on_terminator ---->", hex(addresses[0])
        hir_stmt = None

        if isinstance(mir_inst, MiddleIrRetInstruction):
            # Handle return statement. Prepare the statement according to the
            # return type (if any).
            if mir_inst.operands is None:
                hir_stmt = ReturnStatement()

            elif len(mir_inst.operands) == 1:
                # In case that the return instruction returns a value (not
                # void) then the return type must be obtained and processed.
                ret_op = mir_inst.operands[0]

                if isinstance(ret_op, MiddleIrInstruction):
                    ret_op = self.transform_mir_to_hir(ret_op)
                    # Add addresses from inner instruction.
                    addresses += ret_op.addresses
                    ret_val = str(ret_op)
                elif isinstance(ret_op, MiddleIrBaseConstant):
                    #ret_tuple = str(ret_op).split(" ") # split the type and name.
                    #ret_type, ret_val = ret_tuple
                    ret_val = ret_op.value
                else:
                    raise CBackEndException("Unable to process operand (%s)" % \
                        ret_op)
                    
                hir_stmt = ReturnStatement(ret_val)
            else:
                raise CBackEndException(
                    "Return statement with multiple values is unimplemented.")

        return hir_stmt

    def on_memory_access(self, mir_inst):
        """Process a MIR 'memory access' instruction."""
        addresses = mir_inst.addresses
        print "on_memory_access ---->", hex(addresses[0])
        hir_stmt = None

        if isinstance(mir_inst, MiddleIrStoreInstruction):
            st_op = mir_inst.value

            if isinstance(st_op, MiddleIrInstruction):
                st_op = self.transform_mir_to_hir(st_op)
                # Add addresses from inner instruction.
                addresses += st_op.addresses
                st_val = str(st_op)

            elif isinstance(st_op, MiddleIrBaseConstant):
                #ret_tuple = str(st_op).split(" ") # split the type and name.
                #ret_type, ret_val = ret_tuple
                st_val = st_op.value

            elif isinstance(st_op, MiddleIrArgument):
                #st_op = self.transform_mir_to_hir(st_op.name)
                # Add addresses from inner instruction.
                #addresses += st_op.addresses
                st_val = st_op.get_readable_inners()

            else:
                raise CBackEndException("Unable to process operand (%s)" % \
                    st_op)

            hir_stmt = ExpressionStatement(
                SimpleAssignmentExpression(
                    mir_inst.pointer.get_readable_inners(),
                    st_val),#mir_inst.value.get_readable_inners()),
                addresses)

        elif isinstance(mir_inst, MiddleIrLoadInstruction):
            hir_stmt = ExpressionStatement(
                Expression(
                    mir_inst.pointer.get_readable_inners()),
                addresses)

        return hir_stmt

    def on_conversion(self, mir_inst):
        """Process a MIR 'conversion' instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None
        print "on_conversion ---->", hex(addresses[0])

        #if isinstance(mir_inst, MiddleIrIntToPtrInstruction):
        #    hir_stmt = ExpressionStatement(
        #        SimpleAssignmentExpression(
        #            mir_inst.pointer.get_readable_inners(),
        #            mir_inst.value.get_readable_inners()),
        #        mir_inst.addresses)

        #if isinstance(mir_inst, MiddleIrPtrToIntInstruction):
        #    pass

        return hir_stmt

    def on_binary(self, mir_inst):
        """Process a MIR 'binary' instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None
        print mir_inst
        print "on_binary ---->", " - ".join(["0x%X" % x for x in addresses])

        if isinstance(mir_inst, MiddleIrAddInstruction):
            if isinstance(mir_inst.rhs, MiddleIrBaseConstant):
                rhs = IntegerLiteralExpression(mir_inst.rhs.get_readable_inners())
            else:
                rhs = mir_inst.rhs.get_readable_inners()

            if isinstance(mir_inst.lhs, MiddleIrBaseConstant):
                lhs = IntegerLiteralExpression(mir_inst.lhs.get_readable_inners())
            else:
                lhs = mir_inst.lhs.get_readable_inners()

            hir_stmt = Statement(
                BinaryExpression(
                    lhs,
                    "+",
                    rhs),
                addresses)

        elif isinstance(mir_inst, MiddleIrSubInstruction):
            if isinstance(mir_inst.rhs, MiddleIrBaseConstant):
                rhs = IntegerLiteralExpression(mir_inst.rhs.get_readable_inners())
            else:
                rhs = mir_inst.rhs.get_readable_inners()

            if isinstance(mir_inst.lhs, MiddleIrBaseConstant):
                lhs = IntegerLiteralExpression(mir_inst.lhs.get_readable_inners())
            else:
                lhs = mir_inst.lhs.get_readable_inners()

            hir_stmt = Statement(
                BinaryExpression(
                    lhs,
                    "-",
                    rhs),
                addresses)

        return hir_stmt

    def on_other(self, mir_inst):
        """Process a MIR 'other' instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None

        if isinstance(mir_inst, MiddleIrCallInstruction):
            arguments = mir_inst.get_readable_inners()
            hir_stmt = Statement(
                FunctionCallExpression(mir_inst.callee.name, arguments),
                addresses)

        return hir_stmt

    def __display_instruction_information(self, hir_stmt, hir_group):
        """Print information about the assembler instruction specified which
        belong to the group parameter.

        """
        if self.debug_inst_info:

            addresses = "\n\t".join(
                ["0x%08x" % addr for addr in hir_stmt.addresses if not None])
            group = hir_group.capitalize()
            stmt_type = hir_stmt.type
            stmt_repr = "BLABLA" #hir_stmt._ptr.opcode_name

            print "\t%(addresses)s %(group)15s " \
                  "(type %(stmt_type)3d) - %(stmt_repr)-25s" % vars()

    def analyze(self):
        """Perform all the corresponding back-end analysis and finally generate
        the HIR representation (only 'C' language is implemented).
        
        """
        #
        # Step x
        #
        # Perform any appropriate analysis before HIR generation process
        # begins.
        #
        # TODO : Do analysis here.

        #
        # Step x
        #
        # Create the high level IR used for final representation.
        #
        print "[+] Creating High level IR..."
        self.generate_hir()

    def generate_output(self):
        """Generate a final output."""
        # Create an output instance to display the current C code
        # representation hosted inside the HIR.
        print "[+] Creating HIR representation..."
        print str(self.hir_function)
        #return
        hir_output = HirTextOutput(self.hir_function)
        hir_output.generate_output("Decompiled code")

    def map_mir_type_to_hir_repr(self, mir_type):
        """Return the HIR string representation of the given MIR type."""
        return MIR_TYPE_TO_HIR_STRING.get(type(mir_type), None)

