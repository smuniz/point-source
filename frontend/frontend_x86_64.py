# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

#import idioms_x86_64_gcc
#reload(idioms_x86_64_gcc)
from idioms_x86_64_gcc import X86_64GccIdiomAnalyzer
from misc.prerequisites import require

# Import MIR related modules
from middleend.mir import *


class FrontEndX86_64Exception(Exception):
    pass


class FrontEndX86_64(FrontEnd):
    """
    Front-end support for the PowerPC architecture.
    """

    TARGET_ARCH = "x86_64"

    def __init__(self, debugger):
        """Perform X86_64 front-end instance initialization."""
        FrontEnd.__init__(self, X86_64GccIdiomAnalyzer, debugger)

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
