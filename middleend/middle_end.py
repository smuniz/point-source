# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import mir.mir_text_output
reload(mir.mir_text_output)
from mir.mir_text_output import MirTextOutput

__all__ = ["MiddleEnd", "MiddleEndException"]


class MiddleEndException(Exception):
    """Generic exception for middle-end analysis."""
    pass


class MiddleEnd(object):
    """It provides support for architecture independant analysis and performs
    the core of the decompiling analysis.

    Two phases are included in this module, the data flow and the cotrol flow
    analyzers.

    """

    def __init__(self, mir_module=None):
        self.mir = mir_module

    @property
    def mir(self):
        """Return the intermediate level presentation ofthe current function
        being decompiled.
        """
        return self.mir_module

    @mir.setter
    def mir(self, mir_module):
        """Store the intermediate level presentation ofthe current function
        being decompiled.
        """
        self.mir_module = mir_module

    def perform_control_flow_analysis(self):
        """Execute the Control Flow analysis and any post-analysis depending on
        it.
        """
        print "[+] Initiating control flow analysis..."
        # TODO: implement this

    def perform_data_flow_analysis(self):
        """
        This phase attemps to improve the intermediate code, so that high-level
        language expression can be found.

        The use of temporary registers and condition flags is eliminated during
        this analysis, as these concepts are not available in high-level
        languages.
        """
        print "[+] Initiating data flow analysis..."

        if not self.mir:
            raise MiddleEndException(
                "The Middle-end IR was not specified.")

        self.dead_register_elimination_analysis()

        self.dead_condition_elimination_analysis()

        self.condition_code_propagation_analysis()

        self.register_arguments_analysis()

        self.function_return_registers_analysis()

    def dead_register_elimination_analysis(self):
        """
        A register is dead if it is defined by an instructions and it is not
        used before being redefined by a subsequent instruction.
        If the instruction that defines a dead registers defines only this one
        register, it is said that the instruction is useless, and thus, is
        eliminated.
        On the other hand, if the instruction also defines other(s) registers,
        the instruction then it's still useful but should not define the dead
        register(s) any more.
        """
        # TODO: implement this
        pass

    def dead_condition_elimination_analysis(self):
        # TODO: implement this
        pass

    def condition_code_propagation_analysis(self):
        # TODO: implement this
        pass

    def register_arguments_analysis(self):
        # TODO: implement this
        pass

    def function_return_registers_analysis(self):
        # TODO: implement this
        pass

    def extract_registers_from_expression(self, expr):
        """Given the current expression, analyze it to obtain the operands in
        use.
        """
        """
        r_ops = []

        if isinstance(expr, BinaryExpression):

            l_sub_op = expr.left_operand
            r_sub_op = expr.right_operand

            if isinstance(r_sub_op, TemporalStorage):
                r_ops.append(r_sub_op)

            if isinstance(l_sub_op, TemporalStorage):
                r_ops.append(l_sub_op)

        elif isinstance(expr, PrimaryExpression):
            pass

        elif isinstance(expr, TemporalStorage):
            r_ops.append(expr)

        return r_ops
        """
        pass

    def generate_output(self):
        """Generate a debugging output with the UD and DU chains."""
        print "[+] Generating MIR representation..."
        #print self.mir
        #return
        # Create an output instance to display the current LLVM IR
        # representation hosted inside the MIR.
        mir_output = MirTextOutput(self.mir)
        mir_output.generate_output("LLVM IR output")
