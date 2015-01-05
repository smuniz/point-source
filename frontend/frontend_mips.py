# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

import idioms_mips_gcc
reload(idioms_mips_gcc)
from idioms_mips_gcc import MipsGccIdiomAnalyzer

# Import MIR related modules
from middleend.mir import *


class FrontEndMipsException(Exception):
    """Generic MIPS front-end exception."""
    pass


class FrontEndMips(FrontEnd):
    """Front-end support for the MIPS architecture."""

    TARGET_ARCH = "mips"

    def __init__(self, debugger):
        """Perform MIPS front-end instance initialization."""
        FrontEnd.__init__(self, MipsGccIdiomAnalyzer, debugger)

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
