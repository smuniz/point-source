#
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from frontend import FrontEnd

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
        super(FrontEndX86, self).__init__(debugger)

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

    def _extract_callee_address(self, lir_inst):
        """Return the callee address from a call instruction, if any."""
        if not self.idiom_analyzer.is_call_instruction(lir_inst):
            return None

        # FIXME This was copied from PPC without any testing... check it
        #if len(lir_inst) == 1:
        #    return lir_inst[0].value

        return None

    #def analyze_callee(self, callee_address):
    #    """Analyze the callee function by performing a live analysis on it."""
    #    lir_function = self.debugger.generate_lir(callee_address)
    #    #print lir_function
    #    return lir_function

    def _is_stack_destination(self, lir_inst):
        """Check that destination of the operation is the stack."""
        # TODO
        return False
