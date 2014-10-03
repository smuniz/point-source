# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

"""
Types of supported statements:

    * labeled statements
          - identifier labels
          - case labels
          - default labels 
    * expression statements
    * block or compound statements
    * selection statements
          - if statements
          - switch statements 
    * iteration statements
          - while statements
          - do statements
          - for statements 
    * jump statements
          - break statements
          - continue statements
          - return statements
          - goto statements 
    * declaration statements
    * (C++)try blocks 
"""

from graph import Graph
from area import Area
from expressions import Expression


class Statement(Area):
    """A statement, the smallest independent computational unit, specifies an
    action to be performed.

    """

    def __init__(self, expression=None, addresses=None):
        super(Statement, self).__init__(addresses)

        self.expression = expression
        self.removed = False
        #self.has_expression = has_expression

    def set(self, expression):
        self.expression = expression

    def get(self):
        return self.expression

    @property
    def removed(self):
        return self._removed

    @removed.setter
    def removed(self, removed):
        self._removed = removed

    #@property
    #def has_expression(self):
    #    return self._has_expression

    #@has_expression.setter
    #def has_expression(self, has_expression):
    #    self._has_expression = bool(has_expression)


class CompoundStatement(object): #Statement): #, Graph):
    """A block statement, or compound statement, lets you group any number of
    data definitions, declarations, and statements into one statement.

    All definitions, declarations, and statements enclosed within a
    single set of braces are treated as a single statement.

    """

    def __init__(self, addresses=None, in_edges=None, out_edges=None):
        #super(CompoundStatement, self).__init__(addresses=addresses)
        #Statement.__init__(self, addresses)
        #Graph.__init__(self, in_edges, out_edges)

        self.statements = list()
        self.label = None
        #self.current = 0

    @property
    def statements(self):
        return self._statements

    @statements.setter
    def statements(self, statements):
        self._statements = statements

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    def add_statement(self, statement, index=None):
        """Add the new statement parameter at the specified position."""
        if index is None:
            index = len(self.statements)
        self.statements.insert(index, statement)

    def get_statement(self, index):
        """Return the statement at the speificied position."""
        return self.statements[index]

    def remove_statement(self, statement):
        """Given the specified statement, find it's position inside the list of
        all processed statements and remove it from the list using the obtained
        position.

        """
        try:
            for stmt in self:
                if stmt == statement:
                    pos = self.statements.index(stmt)
                    del self.statements[pos]
                    return True
        except:
            return False

    #def get_statement_by_address(self, address):
    #    for st in self.statements:
    #        if st is None:
    #            print "------> 0x%X" % address
    #        if st.hasAddress(address):
    #            return st
    #    return None

    #def remove_statement_by_address(self, address):
    #    st = self.get_statement_by_address(address)

    #    if st is not None:
    #        pos = self.statements.index(st)
    #        del self.statements[pos]
    #        return True
    #    else:
    #        return False

    #def __setitem__(self, key, item):
    #    if isinstance(key, slice):
    #        print "__setitem__ not yet implemented with slice type"
    #    elif isinstance(key, (int, long)):
    #        FIX THIS CODE
    #        self.expression = item, key
    #    else:
    #        raise TypeError

    #def __getitem__(self, key):
    #    if isinstance(key, slice):
    #        indices = key.indices(len(self))
    #        return [self[i] for i in xrange(*indices)]
    #    elif isinstance(key, (int, long)):
    #        try:
    #            return self.get(key)
    #        except KeyError:
    #            raise IndexError
    #    else:
    #        raise TypeError

    def __len__(self):
        return len(self.statements)

    #def __iter__(self):
    #    self.current = 0
    #    return self

    #def next(self):
    #    if self.current < len(self):
    #        i = self[self.current]
    #        self.current += 1
    #        return i
    #    else:
    #        raise StopIteration

    def __str__(self):
        _str = ""

        # Walk through all the statements and get each one of them.
        for stmt in self.statements:
            _str += str(stmt)

        return _str


class LabelStatement(Statement):
    """To transfer program control directly to a given statement, the statement
    must be labeled.

    There are three kinds of labels: identifier, case, and default.

    """
    # Local label used by low-level branch instructions.
    # Should only be used if control-flow analysis was unsuccsessful.
    def __init__(self, name=None, addresses=None):
        super(LabelStatement, self).__init__(addresses=addresses)
        if name is not None:
            self.expression = name
        else:
            self.expression = "unk_label"


class IdentifierLabelStatement(LabelStatement):
    """The appearance of an identifier label in the source program declares a
    label. Only a goto statement can transfer control to an identifier label.

    """
    def __init__(self, name):
        super(IdentifierLabelStatement, self).__init__(name)

    def __str__(self):
        return "%s : " % self.expression


class ExpressionStatement(Statement):
    """Expression statements cause expressions to be evaluated. No transfer of
    control or iteration takes place as a result of an expression statement.

    """
    def __init__(self, addresses=None):
        super(ExpressionStatement, self).__init__(addresses=addresses)


class GotoStatement(Statement):
    """A goto statement causes your program to unconditionally transfer control
    to the statement associated with the label specified on the goto statement.

    """
    def __init__(self, addresses=None):
        super(GotoStatement, self).__init__(addresses=addresses)

    def __str__(self):
        return "goto loc_%X" % self.expression


class ReturnStatement(Statement):
    """A return statement ends the processing of the current function and
    returns control to the caller of the function.
    
    """
    def __init__(self, expression=None, addresses=None):
        super(ReturnStatement, self).__init__(
            expression=expression, addresses=addresses)

    def __str__(self):
        if self.expression:
            return "return 0x%x;" % self.expression
        else:
            return "return;"
