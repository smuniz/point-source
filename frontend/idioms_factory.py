# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from misc.factory import Factory, FactoryException

import idioms_mips_gcc
reload(idioms_mips_gcc)
from idioms_mips_gcc import MipsGccIdiomAnalyzer

import idioms_powerpc32_gcc
reload(idioms_powerpc32_gcc)
from idioms_powerpc32_gcc import PowerPc32GccIdiomAnalyzer

import idioms_x86_64_gcc
reload(idioms_x86_64_gcc)
from idioms_x86_64_gcc import X86_64GccIdiomAnalyzer

import idioms_x86_gcc
reload(idioms_x86_gcc)
from idioms_x86_gcc import X86GccIdiomAnalyzer

import idioms_arm_gcc
reload(idioms_arm_gcc)
from idioms_arm_gcc import ArmGccIdiomAnalyzer

import idioms_aarch64_gcc
reload(idioms_aarch64_gcc)
from idioms_aarch64_gcc import AArch64GccIdiomAnalyzer

__all__ = ["IdiomsFactory", "IdiomsFactoryException"]


class IdiomsFactoryException(FactoryException):
    """Idioms factory base exception class."""
    pass


class IdiomsFactory(Factory):
    """
    Factory for different idioms to support multiple compilers under multiple
    CPU architectures.

    """

    def __init__(self):
        """Perform factory instance initialization."""
        #
        # Register known idioms for further creation.
        #
        # This is where any new compilers should be registered (appart from its
        # support under the current debugger).
        #
        self.register("create_GCC_x86", X86GccIdiomAnalyzer)
        self.register("create_GCC_x86_64", X86_64GccIdiomAnalyzer)
        self.register("create_GCC_ARM", ArmGccIdiomAnalyzer)
        self.register("create_GCC_AArch64", AArch64GccIdiomAnalyzer)
        self.register("create_GCC_MIPS", MipsGccIdiomAnalyzer)
        self.register("create_GCC_PowerPC", PowerPc32GccIdiomAnalyzer)

