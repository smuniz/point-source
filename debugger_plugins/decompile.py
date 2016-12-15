#!/usr/bin/env python
"""

(c) Sebastian Muniz 2017

Point Source decompiler init script for Immunity Debugger

"""

try:
    import immlib
except ImportError, err:
    # Intentionally display error using standard python output function 
    # because immlib couldn't be loaded.
    print "[-] This module must be executed inside Immunity Debugger."

from traceback import format_exc

# Needed by immdbg to load PyCommands list information.
#NAME = "main"
__VERSION__ = '0.1'
__description__ = "Point Source Decompiler"

DESC = __description__

def usage(imm):
    """Display all the usage options."""

    imm.log("", focus = 1)
    imm.log("%s" % DESC)
    imm.log("=" * len(DESC))
    imm.log("")
    imm.log("usage: !%s" % __name__)
    imm.log("")

def main(args):
    """Main function used to invoke the decompiler."""

    imm = immlib.Debugger()

    from sys import path
    path_to_add = r"y:\decompiler\decompilers\point source"

    if path_to_add not in path:
        path.append(path_to_add)

    #import test_immdbg
    #imm.log("===> %s" % test_immdbg)
    #from test_immdbg import main as test_main
    import pointsource
    imm.log("===> %s" % pointsource)
    from pointsource import main as test_main

    test_main()

    try:
        # FIXME: Remove this hardcoded path and get it dynamically from
        # somewhere else.
        #ret = execfile(r"y:\decompiler\decompilers\point source\pointsource.py")
        ret = "Decompiler execution finished"

    except Exception, err:
        imm.log("[-] Error on:", focus = 1)

        imm.logLines(format_exc())

        ret = err
        
    return ret
