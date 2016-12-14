# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_aarch64_gcc
reload(idioms_aarch64_gcc)
from idioms_aarch64_gcc import AArh64GccIdiomAnalyzer

# Import MIR related modules
from middleend.mir import *


class FrontEndAArh64Exception(Exception):
    """Generic ARM front-end exception."""
    pass


class FrontEndAArh64(FrontEnd):
    """Front-end support for the AArch (ARM 64-bits) architecture."""

    TARGET_ARCH = "aarch64"

    def __init__(self, debugger):
        """Perform ARM front-end instance initialization."""
        FrontEnd.__init__(self, AArh64GccIdiomAnalyzer, debugger)

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
