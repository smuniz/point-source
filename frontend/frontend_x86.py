# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

#import idioms_x86_gcc
#reload(idioms_x86_gcc)
from idioms_x86_gcc import X86GccIdiomAnalyzer
from misc.prerequisites import require

# Import MIR related modules
from middleend.mir import *


class FrontEndX86Exception(Exception):
    pass


class FrontEndX86(FrontEnd):
    """
    Front-end support for the PowerPC architecture.
    """

    TARGET_ARCH = "x86"

    def __init__(self, debugger):
        """Perform X86 front-end instance initialization."""
        FrontEnd.__init__(self, X86GccIdiomAnalyzer, debugger)

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
