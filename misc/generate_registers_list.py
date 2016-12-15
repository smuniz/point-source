#!/bin/env python
from sys import exit

try:
    import idaapi
except ImportError, err:
    print "This script only runs under IDA-Python."
    exit(1)

def main():
    # Obtain a list of the registers for the current architecture.
    regs = idaapi.ph_get_regnames()

    for i, reg in enumerate(regs):
        print "    %-5s = %d" % (reg.upper(), i)

    # Add a separator
    print "\n    TOTAL_GPR = %d" % len(regs)

    # Now create a list of the the previous enumerated registers and put them
    # under the GPR (General Porpuse Registers) name).
    print "\n    GPR_NAMES = {"

    for i, reg in enumerate(regs):
        print "        %-5s = \"%s\"" % (reg.upper(), reg)

    print "\n    }"

if __name__ == "__main__":
    main()
