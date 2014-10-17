# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class Stack(object):
    """
    Perform a detailed representation of the stack of the function analyzed.
    Even though the information on this class is very detailed it's related to
    all the architectures supported by the decompiler.

    """

    def __init__(self, stack_register=None):
        self.stack_register = stack_register

    @property
    def stack_register(self):
        return self._stack_register

    @stack_register.setter
    def stack_register(self, stack_register):
        self._stack_register = stack_register


