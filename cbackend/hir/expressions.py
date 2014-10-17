# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from operators import *
from area import Area


class Expression(Area):
    """Generic expression class."""

    def __init__(self, value=None, addresses=None):
        super(Expression, self).__init__(addresses)
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

    def __str__(self):
        if self.get() is None:
            return "<gen.expr=None>"
        else:
            return "%s" % self.get()


class UnaryExpression(Expression):
    """Unary expression class."""

    def __init__(self):
        super(UnaryExpression, self).__init__()

    def __str__(self):
        return "// unary expression __str__ not implemented"


class IndirectionUnaryExpression(UnaryExpression):
    """Indirection on Unary expression class."""
    def __init__(self):
        super(IndirectionUnaryExpression, self).__init__()

    def __str__(self):
        return "*%s" % self.get()


class BinaryExpression(Expression):
    """Binary expression class."""

    def __init__(self):
        super(BinaryExpression, self).__init__()

    def set(self, left_operand, operator, right_operand):
        self.left_operand   = left_operand
        self.right_operand  = right_operand
        self.operator       = operator

    def __str__(self):
        return "(%s %s %s)" % (self.left_operand, self.operator, 
                            self.right_operand)


class AssignmentExpression(Expression):
    """An assignment expression stores a value in the object designated by the
    left operand. There are two types of assignment operators: Simple
    assignment and Compound assignment.

    """

    def __init__(self):
        super(AssignmentExpression, self).__init__()
        self.operator = SimpleAssignmentOperator()


class SimpleAssignmentExpression(AssignmentExpression):
    """
    The simple assignment operator has the following form:

    lvalue = expr

    The operator stores the value of the right operand expr in the object
    designated by the left operand lvalue. 

    """
    def __init__(self):
        super(SimpleAssignmentExpression, self).__init__()
        self.set(None, None)

    def set(self, left_operand, right_operand):
        self.left_operand   = left_operand
        self.right_operand  = right_operand

    def __str__(self):
        return "%s %s %s" % (self.left_operand, self.operator, 
                            self.right_operand)


class CompoundAssignmentExpression(AssignmentExpression):
    """The compound assignment operators consist of a binary operator and the
    simple assignment operator. They perform the operation of the binary
    operator on both operands and store the result of that operation into the
    left operand, which must be a modifiable lvalue.
    
    """

    def __init__(self):
        super(CompoundAssignmentExpression, self).__init__()
        self.set(None, None)

    def set(self, left_operand, right_operand, operator):
        self.left_operand   = left_operand
        self.right_operand  = right_operand
        self.operator       = operand

    def __str__(self):
        return "%s %s %s" % (self.left_operand, self.operator, 
                            self.right_operand)


class UnknownExpression(Expression): 
    """Unknown expression class."""
    def __init__(self, value=None):
        super(UnknownExpression, self).__init__(value)

    def __str__(self):
        output = "// %s at %s" % (self.value, \
                " ".join(["0x%X" % addr for addr in self.addresses]))
        return output


class PrimaryExpression(Expression):
    """..."""
    def __init__(self, value=None):
        super(PrimaryExpression, self).__init__(value)


class LiteralExpression(PrimaryExpression):
    """
    A literal is a constant primary expression. Its type depends on the form of
    its specification.
    Invariant program elements are called "literals" or "constants." The terms
    "literal" and "constant" are used interchangeably here.
    A literal may be any of the following:

        integer-constant
        character-constant
        floating-constant
        string-literal

    Examples:

        157         // integer constant
        0xFE        // integer constant
        'c'         // character constant
        0.2         // floating constant
        0.2E-01     // floating constant
        "brown dog" // string literal
    """
    def __init__(self, value=None):
        super(LiteralExpression, self).__init__(value)


class IntegerLiteralExpression(LiteralExpression):
    """..."""
    HEX_REPR = "0x%x"
    OCT_REPR = "o%03o"
    DEC_REPR = "%d"

    def __init__(self, value=None):
        super(IntegerLiteralExpression, self).__init__(value)
        self.set_representation(self.HEX_REPR)

    def set_representation(self, repr):
        self.representation = repr
        
    def get_representation(self, repr):
        return self.representation
        
    def __str__(self):
        return self.representation % self.get()


class StringLiteralExpression(LiteralExpression):
    """A string literal contains a sequence of characters or escape sequences
    enclosed in double quotation mark symbols.
    
    """
    def __init__(self, value=None):
        super(StringLiteralExpression, self).__init__(value)

    def __str__(self):
        return "\"%s\"" % repr(self.get())[1:-1] # remove single quotes


class TemporalStorage(Expression):
    """..."""
    def __init__(self, value=None):
        super(TemporalStorage, self).__init__(value)


class FunctionCallExpression(Expression):
    """..."""

    def __init__(self, func_name=None, arguments=[]):
        super(FunctionCallExpression, self).__init__()

        self.set(func_name, arguments)

    def format_values(self, func_name, arguments):
        type_name  = PrimaryExpression(func_name)
        #operator   = FunctionCallOperator()             # useless
        arguments  = ParenthesizedExpression(arguments)
        return [type_name, arguments]

    def set(self, func_name, arguments):
        self.value = self.format_values(func_name, arguments)

    def __str__(self):
        return "%s %s;" % (self.get()[0], self.get()[1])

    
class ParenthesizedExpression(Expression):
    """..."""
    def __init__(self, arguments=[]):
        super(ParenthesizedExpression, self).__init__(arguments)

    def __str__(self):
        return "(%s)" % ", ".join([str(x) for x in self.get()])
