# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class Area(object):
    """An area is an address range used to define the memory region that an
    object (whether it's low-level or higher level representation) occupies.

    """

    def __init__(self, addresses=None):
        # List of addresses belonging to the assembly representation of the
        # program for the current decompiled line.
        if addresses is None:
            self.addresses = list()
        else:
            self.addresses = addresses
            self.addresses.sort()

    @property
    def addresses(self):
        """Return the list of addressess that this object represents."""
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Store the entire list of addresses for the current area."""
        self._addresses = addresses

    def add_address(self, address):
        if not self.has_address(address):
            self._addresses.append(address)
        self._addresses.sort()

    def remove_address(self, address):
        try:
            idx = self._addresses.index(address)
            del self._addresses[idx]
            return True
        except:
            return False

    def has_address(self, address):
        if address in self._addresses:
            return True
        return False

    def get_start_address(self):
        return self._addresses[0]

    def get_end_address(self):
        return self._addresses[-1]
