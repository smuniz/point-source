# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_arm_gcc
reload(idioms_arm_gcc)
from idioms_arm_gcc import ArmGccIdiomAnalyzer

# Import MIR related modules
from middleend.mir import *


class FrontEndArmException(Exception):
    """Generic ARM front-end exception."""
    pass


class FrontEndArm(FrontEnd):
    """Front-end support for the ARM architecture."""

    TARGET_ARCH = "arm"

    def __init__(self, debugger):
        """Perform ARM front-end instance initialization."""
        FrontEnd.__init__(self, ArmGccIdiomAnalyzer, debugger)

    def on_assignment(self, lir_inst):
        """Handle Low level IR assignment instructions."""
        return None

    def on_unconditional_branch(self, lir_inst):
        """Handle Low level IR unconditional branch instructions."""
        return None

    def on_conditional_branch(self, lir_inst):
        """Handle Low level IR conditional branch instructions."""
        return None

    def on_unknown(self, lir_inst):
        """Handle unknown Low level IR instructions."""
        return None
