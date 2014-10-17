# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class Area(object):
    """An area is an address range used to define the memory region that an
    object (whether it's low-level or higher level representation) occupies.

    """

    def __init__(self, addresses=None):
        """Initialize the area instance."""
        # List of addresses belonging to the assembly representation of the
        # program for the current decompiled line.
        if addresses is None:
            self.addresses = list()
        else:
            self.addresses = addresses
            self.addresses.sort()

    @property
    def addresses(self):
        """Return the entire list of addresses for the current area."""
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Store the entire list of addresses for the current area."""
        self._addresses = addresses

    def add_address(self, address):
        """Add the specified address to the addresses list."""
        # Add the address only in case it doesn't exist.
        if address not in self._addresses:
            self._addresses.append(address)

            # Keep the addresses list sorte in ascending order.
            self._addresses.sort()

    def remove_address(self, address):
        """Remove the specified address from the current area."""
        try:
            idx = self._addresses.index(address)
            del self._addresses[idx]
        except IndexError, err:
            return False

        return True
        
    def has_address(self, address):
        """Indicate if the specified address belongs to this area or not."""
        if address in self._addresses:
            return True
        return False

    @property
    def start_address(self):
        """Return the initial address."""
        try:
            return self.addresses[0]
        except IndexError, err:
            pass

        return None

    @property
    def end_address(self):
        """Return the end address."""
        try:
            return self._addresses[-1]
        except IndexError, err:
            pass

        return None
