# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

import frontend_x86
reload(frontend_x86)
from frontend_x86 import FrontEndX86, FrontEndX86Exception

import frontend_x86_64
reload(frontend_x86_64)
from frontend_x86_64 import FrontEndX86_64, FrontEndX86_64Exception

import frontend_arm
reload(frontend_arm)
from frontend_arm import FrontEndArm, FrontEndArmException

import frontend_aarch64
reload(frontend_aarch64)
from frontend_aarch64 import FrontEndAArch64, FrontEndAArch64Exception

import frontend_powerpc
reload(frontend_powerpc)
from frontend_powerpc import FrontEndPowerPc, FrontEndPowerPcException

import frontend_mips
reload(frontend_mips)
from frontend_mips import FrontEndMips, FrontEndMipsException

__all__ = ["FrontEndFactory", "FrontEndFactoryException"]


class FrontEndFactoryException(Exception):
    """Front-end factory base exception class."""
    pass


class FrontEndFactory(object):
    """
    Factory for different front-ends to support multiple decompilable
    architectures.

    """

    def __init__(self, debugger):
        """Perform factory instance initialization."""
        # Register known front-ends for further creation.
        self.register("create_x86", FrontEndX86, debugger)
        self.register("create_x86_64", FrontEndX86_64, debugger)
        self.register("create_ARM", FrontEndArm, debugger)
        self.register("create_AArch64", FrontEndAArch64, debugger)
        self.register("create_MIPS", FrontEndMips, debugger)
        self.register("create_PowerPC", FrontEndPowerPc, debugger)

    def register(self, methodName, constructor, *args, **kargs):
        """register a constructor"""
        _args = [constructor]
        _args.extend(args)
        setattr(self, methodName,apply(Functor,_args, kargs))
        
    def unregister(self, methodName):
        """unregister a constructor"""
        delattr(self, methodName)

class Functor:
    def __init__(self, function, *args, **kargs):
        assert callable(function), "function should be a callable obj"
        self._function = function
        self._args = args
        self._kargs = kargs
        
    def __call__(self, *args, **kargs):
        """call function"""
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return apply(self._function,_args,_kargs)
