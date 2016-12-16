# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from misc.factory import Factory, FactoryException

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


class FrontEndFactoryException(FactoryException):
    """Front-end factory base exception class."""
    pass


class FrontEndFactory(Factory):
    """
    Factory for different front-ends to support multiple decompilable
    architectures.

    """

    def __init__(self):
        """Perform factory instance initialization."""
        #
        # Register known front-ends for further creation.
        #
        # This is where any new architecture should be added (appart from its
        # support under the current debugger).
        #
        self.register("create_x86", FrontEndX86)
        self.register("create_x86_64", FrontEndX86_64)
        self.register("create_ARM", FrontEndArm)
        self.register("create_AArch64", FrontEndAArch64)
        self.register("create_MIPS", FrontEndMips)
        self.register("create_PowerPC", FrontEndPowerPc)
