# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class Operator(object):
    """Basic operator class."""

    def __init__(self, representation=None):
        if representation is None:
            self.representation = "<undef.op.repr>"
        else:
            self.setrepresentationesentation(representation)

    @property
    def representation(self):
        """Return the way to represent this operation when outputting HIR
        information.
        
        """
        return self._representation

    @representation.setter
    def representation(self, representation):
        """Store the way to represent this operation when outputting HIR
        information.
        
        """
        self._representation = representation

    def __str__(self):
        return self.representation


class BinaryOperator(Operator):
    """Binary operator class."""

    def __init__(self, representation=None):
        super(BinaryOperator, self).__init__()

        if representation is None:
            representation = "<Binary Operator>"
        Operator.__init__(self, representation)


class AdditionOperator(BinaryOperator):
    """Addition operator class."""

    def __init__(self):
        super(AdditionOperator, self).__init__("+")
        

class SimpleAssignmentOperator(Operator):
    """The simple assignment operator has the following form:

        lvalue = expr

    The operator stores the value of the right operand expr in the object
    designated by the left operand lvalue.

    """
    def __init__(self):
        super(SimpleAssignmentOperator, self).__init__("=")


class CompoundAssignmentOperator(Operator):
    """The compound assignment operators consist of a binary operator and the
    simple assignment operator. They perform the operation of the binary
    operator on both operands and store the result of that operation into the
    left operand, which must be a modifiable lvalue.

    """
    def __init__(self):
        # Not really needed becuase this class is composed by two operators.
        super(CompoundAssignmentOperator, self).__init__()

        self.assignment_operator = SimpleAssignmentOperator()
        self.binary_operator     = BinaryOperator()
        
    def __str__(self):
        return "%s%s" % (self.binary_operator, self.assignment_operator)


class FunctionCallOperator(Operator):
    """..."""

    def __init__(self):
        super(FunctionCallOperator, self).__init__()
