# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from multidigrah import MultiDiGraph, MultiDiGraphException


class LowLevelBasicBlockException(MultiDiGraphException):
    """Generic exception for the low-level basic block IR."""
    pass


class LowLevelBasicBlock(MultiDiGraph):
    """Handle a list of instructions contained in an araddress with possible
    in/out references from other parts of the program.

    """

    def __init__(self, start_address=None, end_address=None, _id=None):
        """Instance initialization."""
        # Initialize graph.
        super(LowLevelBasicBlock, self).__init__()

        self.instructions = dict()
        self.start_address = start_address

        if end_address == None:
            self.end_address = start_address
        else:
            self.end_address = end_address

        self.current = 0  # iterator counter

        self.function = None

        self._successors = set() # List of successors
        self._predecessors = set() # List of predecessors

        self.id = _id

        self.dom = set()
        self.visited = False # FIXME horrible kludge

    def __eq__(self, other):
        """Override the default Equals behavior"""
        #print "=== eq (%d)" % self.id
        if isinstance(other, self.__class__):
            return self.id == other.id
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        #print "=== ne (%d)" % self.id
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __lt__(self, other):
      # return comparison
        #print "=== lt (%d) < %d" % (self.id, other.id)
        if isinstance(other, self.__class__):
            return self.id < other.id
        return NotImplemented

    def __le__(self, other):
      # return comparison
        #print "=== le (%d)" % self.id
        if isinstance(other, self.__class__):
            return self.id <= other.id
        return NotImplemented

    def __gt__(self, other):
      # return comparison
        #print "=== gt (%d)" % self.id
        if isinstance(other, self.__class__):
            return self.id > other.id
        return NotImplemented

    def __ge__(self, other):
      # return comparison
        #print "=== ge (%d)" % self.id
        if isinstance(other, self.__class__):
            return self.id >= other.id
        return NotImplemented

# TODO : To improve performance it is know directly accessed from the outside.
#    @property
#    def id(self):
#        """Indicate the current basic block ID."""
#        return self._id
#
#    @id.setter
#    def id(self, _id):
#        """Store the current basic block ID."""
#        self._id = _id
#
    def successors(self):
        """"Return a list of every successor stored."""
        return self._successors

    def predecessors(self):
        """"Return a list of every predecessor stored."""
        return self._predecessors

    def add_successor(self, bb):
        """Add a successor basic block to the current one."""
        if not isinstance(bb, LowLevelBasicBlock):
            raise LowLevelBasicBlockException(
                "Unable to add successor basic block of type %r" % \
                type(bb))
        self._successors.add(bb)

    def add_predecessor(self, bb):
        """Add a predecessor basic block to the current one."""
        if not isinstance(bb, LowLevelBasicBlock):
            raise LowLevelBasicBlockException(
                "Unable to add predecessor basic block of type %r" % \
                type(bb))
        self._predecessors.add(bb)

    @property
    def function(self):
        """Indicate the current function it belongs to."""
        return self._function

    @function.setter
    def function(self, function):
        """Store the current function it belongs to."""
        self._function = function

    @property
    def start_address(self):
        return self._start_address

    @start_address.setter
    def start_address(self, address):
        self._start_address = address

    @property
    def end_address(self):
        return self._end_address

    @end_address.setter
    def end_address(self, address):
        self._end_address = address

    def has_address(self, address):
        return self.start_address <= address <= self.end_address

    def add_instruction(self, address, inst):
        self.instructions[address] = inst

        # Sort all the instruction by its addresses.
        self.instructions.keys().sort()

        # The instruction with the smaller address is considered the start
        # address of the basic block.
        if self.start_address is None or address < self.start_address:
            self.start_address = address

        # The instruction with the bigger address is considered the start
        # address of the basic block.
        if self.end_address == 0 or address > self.end_address:
            self.end_address = address

        # Add a cross reference to ourselves.
        inst.basic_block = self

    def get_instruction(self, n):
        k = self.instructions.keys()
        k.sort()

        if n >= len(k):
            raise IndexError

        return self.instructions[k[n]]

    def get_instruction_by_address(self, address):
        """Return the instruction at the specified memory address."""
        if address in self.instructions:
            return self.instructions[address]

        raise LowLevelBasicBlockException(
            "No instruction for specified address 0x%X" % address)

    def get_instruction_index(self, inst):
        """Return the instruction position inside the current basic block
        according to the specified instruction.

        """
        for index, cur_inst in enumerate(self):

            if cur_inst == inst:
                return index

        return None

    def __getitem__(self, key):
        """Return the instruction(s) matching the specified index(es)."""
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]

        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_instruction(key)
            except KeyError:
                raise IndexError

        else:
            raise TypeError

    def __len__(self):
        """Return the count of instructions currently stored."""
        return len(self.instructions)

    def __iter__(self):
        self.current = 0
        return self

    def next(self):
        if self.current < len(self):
            i = self[self.current]
            self.current += 1
            return i
        else:
            raise StopIteration

    def __str__(self):
        """Return the basic block string representation."""
        function_repr = ""
        function_repr += "loc_%08X:\n\n" % self.start_address

        # Get all the instruction inside this basic block.
        function_repr += "\n".join([str(inst) for inst in self])

        return function_repr
