# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from copy import deepcopy
from traceback import format_exc

from middleend.mir.mir_type import *
from middleend.mir.mir_instruction import *

import cbackend.hir.area
reload(cbackend.hir.area)
from cbackend.hir.area import Area

import cbackend.hir.graph
reload(cbackend.hir.graph)
from cbackend.hir.graph import Graph

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
        self.hir = None

        self.function_name = None
        self.function_address = None

        self.label_indent = self.DEFAULT_LABEL_INDENT

        # Development flags
        self.debug_inst_info = True

    @property
    def mir(self):
        """Return the intermediate language representation of the currently
        selected function to be shown.
        
        """
        return self._mir

    @mir.setter
    def mir(self, mir):
        """Store the intermediate language representation of the currently
        selected function to be shown.
        
        """
        self._mir = mir

    @property
    def hir(self):
        """Return the high level IR."""
        return self._hir

    @hir.setter
    def hir(self, hir):
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
            mir_function = self.mir.get_function_by_address(
                self.function_address) 

            # self.hir must contain a global scope and the newly created
            # function in it.
            self.hir = Function()

            # Pass addresses for instruction tracking purposes.
            for address in mir_function.prologue_addresses:
                self.hir.add_prologue_address(address)

            for address in mir_function.epilogue_addresses:
                self.hir.add_epilogue_address(address)

            #
            # Get all the information for the function declaration.
            #
            self.hir.name = mir_function.name

            if isinstance(mir_function.return_type, MiddleIrTypeInt):
                self.hir.return_type = "int"
            elif isinstance(mir_function.return_type, MiddleIrTypeVoid):
                self.hir.return_type = "void"
            else:
                raise CBackEndException("Unsupported return type (%s)" % \
                    mir_function.return_type)


            #
            # Iterate through every basic block represented in the MIR and
            # create its HIR equivalent (block statement) with the appropriate
            # statements and expressions inside.
            #
            hir_block_stmt = CompoundStatement()
            self.hir.add_block(hir_block_stmt)

            for bb_idx, mir_basic_block in enumerate(mir_function):
                #print "-> Basic block %d (%s):%s" % (
                #    bb_idx, mir_basic_block.label, mir_basic_block)

                hir_block_stmt.label = mir_basic_block.label

                for mir_inst in mir_basic_block:
                    #
                    # This step is very important.
                    # This is where most of the MIR instruction are translated
                    # to its HIR equivalents for further usage.
                    #
                    hir_stmt = self.transform_to_hir(mir_inst)

                    if hir_stmt is not None:
                        # Now the newly created instruction is stored in a basic
                        # block, whose purpose is to represent a group of
                        # instructions altogether.
                        hir_block_stmt.add_statement(hir_stmt)

                        # Copy all graph information from low-level representation to the
                        # intermediate-level language.
                        #self.__propagate_graph_information()

        except Exception, err:
            print format_exc()

            raise CBackEndException(
                "High level IR code generation failed : %s" % err)

    def transform_to_hir(self, mir_inst):
        """Get the corresponding HIR statement according to the MIR
        instruction.

        This is language-specific.

        """
        #
        # First we check if the instruction at the current address was
        # previously analyzed and marked for convertion by the idiom analyzer.
        #
        #if self.action_plan.has_plan_for_address(mir_inst.address):
        #    pass

        #
        # Dispatch the current MIR instruction to be appropriate type
        # convertion routine to be transformed into its equivalent HIR
        # statement(s).
        #
        hir_stmt = None
        group_name = mir_inst.group_name

        if mir_inst.group is TERMINATOR_GROUP:
            hir_stmt = self.on_terminator(mir_inst)

        elif mir_inst.group is MEMORY_ACCESS_GROUP:
            hir_stmt = self.on_memory_access(mir_inst)

        elif mir_inst.group is OTHER_GROUP:
            hir_stmt = self.on_other(mir_inst)

        if hir_stmt is None:
            raise CBackEndException(
                "Unsupported instruction (%s) at %s on '%s' group." % (
                    str(mir_inst).strip(),
                    ", ".join(["0x%08X" % a for a in mir_inst.addresses]),
                    group_name))

        # Check if the translation mechanism worked. In case it didn't we;ll
        # raise an exception and notify the user about the offending
        # instruction.
        #
        # This should be submitted for analysis in case that the user agrees.
        #
        if hir_stmt is None:
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

        self.__display_instruction_information(mir_inst, group_name)

        return hir_stmt

    def on_terminator(self, mir_inst):
        """Process a MIR terminator instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None

        if len(mir_inst.operands) > 0:

            ret_op = mir_inst.operands[0]
            ret_tuple = str(ret_op).split(" ")

            if len(ret_tuple) != 2:
                raise CBackEndException("Unable to process operand (%s)" % \
                    ret_op)

            ret_type, ret_val = ret_tuple
            hir_stmt = ReturnStatement(int(ret_val))
        else:
            hir_stmt = ReturnStatement()

        return hir_stmt

    def on_memory_access(self, mir_inst):
        """Process a MIR 'memory access' instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None

        if isinstance(mir_inst, MiddleIrStoreInstruction):
            arguments = mir_inst.get_readable_inners()
            hir_stmt = Statement(
                SimpleAssignmentExpression(
                    mir_inst.pointer.get_readable_inners(),
                    mir_inst.value.get_readable_inners()),
                mir_inst.addresses)

        return hir_stmt

    def on_other(self, mir_inst):
        """Process a MIR 'other' instruction."""
        addresses = mir_inst.addresses
        hir_stmt = None

        if isinstance(mir_inst, MiddleIrCallInstruction):
            arguments = mir_inst.get_readable_inners()
            hir_stmt = Statement(
                FunctionCallExpression(mir_inst.callee.name, arguments),
                mir_inst.addresses)

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
            stmt_repr = hir_stmt._ptr.opcode_name

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
        print str(self.hir)
        return
        hir_output = HirTextOutput(self.hir)
        hir_output.generate_output("Decompiled code")
