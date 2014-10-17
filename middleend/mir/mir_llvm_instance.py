# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class MiddleIrLLVMInstance(object):
    """Middle IR class to hold internal LLVM object reference."""

    def __init__(self, ptr=None):
        """Initialize instance."""
        self._ptr = ptr

    @property
    def _ptr(self):
        """Return MIR type."""
        return self._llvm_ptr

    @_ptr.setter
    def _ptr(self, ptr):
        """Store MIR type."""
        self._llvm_ptr = ptr

    def __str__(self):
        """String representation."""
        return str(self._ptr)

