#!/usr/bin/env python
# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from sys import path as sys_path, exit, stdout
from os import walk, sep
#from os.path import realpath, dirname, sep, exists
from time import clock
from traceback import format_exc
from inspect import getfile, currentframe
from traceback import print_exc

import os

# Add path to system paths.
current_filename = getfile(currentframe())

path_to_current_module = os.path.realpath(os.path.dirname(current_filename))

if path_to_current_module not in sys_path:
    print "[+] Fixing Python modules path..."
    sys_path.append(path_to_current_module)

    #
    # FIXME: Hack to work under virtualenv without LLVMPy installed.
    #
    #from platform import system, machine
    #from sys import version_info

    #os_name = system().lower()
    #mach_name = machine().lower()
    #py_ver = "%s.%s" % (version_info.major, version_info.minor)

    #sys_path.append(
    #    path_to_current_module +
    #    "/third-party/%(os_name)s_%(mach_name)s-python_%(py_ver)s" % \
    #    vars())

    #print sys_path

#------------------------------------------------------------------------------
#
# Check pre-requisites to run the decompiler.
#
from misc.prerequisites import require, run_dependancy_check

# Make sure that all the required python modules are installed.
run_dependancy_check()

from logger import logger
#------------------------------------------------------------------------------
#
# Load front-end modules
#
#require("frontend.generic_disasm")
import frontend.generic_disasm
reload(frontend.generic_disasm)

require("frontend.generic_disasm.base")
from frontend.generic_disasm.base import BaseDebuggerException

require("frontend.generic_disasm.idapro.disassembler")

#import frontend.frontend
#reload(frontend.frontend)
require("frontend.frontend")
from frontend.frontend import FrontEndException

#import frontend.frontendfactory
#reload(frontend.frontendfactory)
require("frontend.frontendfactory")
from frontend.frontendfactory import FrontEndFactory, FrontEndFactoryException

#reload(idioms)
require("frontend.idioms")
#import frontend.idioms as idioms

#import frontend.lir.lir_operand
#reload(frontend.lir.lir_operand)
#from frontend.lir.lir_operand import LowLevelOperand
require("frontend.lir.lir_operand")
#------------------------------------------------------------------------------
#
# Load middle-end modules
#
#import middleend
#reload(middleend)
require("middleend.middle_end")
from middleend.middle_end import MiddleEnd, MiddleEndException

#------------------------------------------------------------------------------
#
# Load C back-end modules
#
#import cbackend
#reload(cbackend)
require("cbackend.c_back_end")
from cbackend.c_back_end import CBackEnd, CBackEndException

#------------------------------------------------------------------------------
__description__ = "Point source decompiler"
__author__      = "Sebastian Muniz"
__year__        = "2013"
__version__     = "0.1"

__all__ = ['PointSource', 'PointSourceException']


class PointSourceException(Exception):
    """Decompiler exception class."""
    pass


class PointSource(object):
    """Decompiler main class."""

    # List of supported output media
    #GRAPH_OUTPUT = 0
    TEXT_OUTPUT = 1

    def __init__(self):#, output_type=TEXT_OUTPUT):
        """Initialization method."""
        # Development flag. Will be more verbose on errors.
        self.__debug = True

        # Store the current debugger instance to interact with the debugger
        # application that invoked us. Used mostly for output.
        self.debugger = None

        # Store the current debugger instance invoking us. This needs to be
        # done really early in the decompilation process because we rely on
        # tons of information provided by the debugger application.
        self.init_debugger_module()

        # Store the target function to decompile.
        self.function_address = None

        # Set the output media use to display decompilation information.
        self.output_type = self.TEXT_OUTPUT#output_type

        self.init_output_media()

        # Front-end holders.
        self.front_end = None
        self.determine_front_end()

    def init_debugger_module(self):
        """Detect the current debugger invoking the decompiler and perform the
        necessary initializations to access the debugger information about the
        binary being decompiled.

        """
        global path_to_current_module
        disassemblers_dir =  sep.join(
            [path_to_current_module, "frontend", "generic_disasm"])

        for root, directories, files in walk(disassemblers_dir):
            # Iterate over every file present in the directory and discard
            # non-python script files.
            for current_dir in directories:
                # Check if the file exists and move to another directory ub
                # case it doesn't.
                _sep = sep
                disasm_py_file = "%(disassemblers_dir)s%(_sep)s" \
                    "%(current_dir)s%(_sep)sdisassembler.py" % vars()

                if not os.path.exists(disasm_py_file):
                    print "No disassembler found in %s" % disasm_py_file
                    continue

                try:
                    # Add current disassembler path for modules lookup.
                    if disassemblers_dir not in sys_path:
                        sys_path.append(disassemblers_dir)

                    # Import the specific disassembler.
                    module_name = "frontend.generic_disasm.%s.disassembler" % current_dir
                    imp_mod = __import__(
                        module_name, globals(), locals(), ["Disassembler"], -1)

                    self.debugger = imp_mod.Disassembler()

                    self.debugger.log("[+] Debugger detected: %s" %
                                  self.debugger.debugger_name)

                    break

                except ImportError, err:
                    # Looks like we've hit an unsupported debugger (this means
                    # that we're not running inside the disassembler we've just
                    # tried to initialize).
                    pass
                except BaseDebuggerException, err:
                    print "Debugger Exception : %s" % err

        # Check if a functional debugger was found. Otherwise abort.
        if not self.debugger:
            raise PointSourceException("Unknown disassembler (if any) in use.")

    @property
    def function_address(self):
        """Return the address of the function being decompiled."""
        return self.func_address

    @function_address.setter
    def function_address(self, address):
        """Store the address of the function being decompiled."""
        self.func_address = address

    def set_screen_address_to_decompile(self):
        """Store the address of the current selected function to decompile."""
        self.function_address = self.debugger.get_current_function_address()

    def init_output_media(self):
        """Initialize the output device used for an enhanced information
        display.

        """
        self.output = None

    def determine_front_end(self):
        """Determine the right front-end for the current architecture."""
        try:
            arch_name = self.debugger.architecture_name
            factory = FrontEndFactory(self.debugger)
            frontend_method = "create_%(arch_name)s" % vars()

            if not hasattr(factory, frontend_method):
                raise PointSourceException(
                    "Unsupported architecture (%s)." % architecture)

            self.front_end_type = getattr(factory, frontend_method)

        except FrontEndFactory, err :
            raise PointSourceException(
                "Unable to detect architecture (%(arch_name)s) : %(err)s" % \
                vars())

    def init_front_end(self):
        """Initialize the front-end of the decompiler."""
        try:
            self.front_end = self.front_end_type()
        except FrontEndFactory, err :
            raise PointSourceException(
                "Unable to initialize front-end : %(err)s" % vars())

        self.log("[+] Loaded front-end is %s" % self.front_end.name)

    def init_middle_end(self):
        """Initialize the middle-end of the decompiler."""
        self.middle_end = MiddleEnd()

    def init_back_end(self):
        """Initialize the back-end of the decompiler."""
        self.back_end = CBackEnd()

    def decompile(self):
        """Decompile the previously specified function."""
        try:
            #self.debugger.display_boxed_message("Decompiling function...")

            # Perform helpers initialization.
            self.init_back_end()
            self.init_middle_end()
            self.init_front_end()

            #
            # Front-end phase
            #
            self.__log_separated("Front-end Phase")

            self.front_end.function_address = self.function_address
            self.front_end.analyze()

            #
            # Middle-end phase
            #
            self.__log_separated("Middle-end Phase")

            self.middle_end.mir = self.front_end.mir

            self.middle_end.perform_control_flow_analysis()
            self.middle_end.perform_data_flow_analysis()

            self.middle_end.generate_output()

            #
            # C Back-end phase
            #
            self.__log_separated("C Back-end Phase")

            optimized_mir = self.middle_end.mir

            self.back_end.function_address = self.function_address
            self.back_end.mir = optimized_mir

            self.back_end.analyze()
            self.back_end.generate_output()

            self.__log_separated("End of decompilation process")

        except BaseDebuggerException, err:
            raise PointSourceException(err)

        except FrontEndException, err:
            raise PointSourceException(err)

        except MiddleEndException, err:
            raise PointSourceException(err)

        except CBackEndException, err:
            raise PointSourceException(err)

        except Exception, err:
            print format_exc()
            raise PointSourceException("Critical error : %s" % err)

        finally:
            # Close the boxed message being displayed on the screen.
            #self.debugger.hide_boxed_message()
            pass

    def __log_separated(self, text):
        """Display a line with the specified text to create a separation in the
        log window.

        """
        sep_length = 80

        filler = "-" * ((sep_length / 2) - (len(text) / 2) - 1)

        self.log("%(filler)s %(text)s %(filler)s" % vars())

    def log(self, text):
        """Display the specified text in the log window."""
        self.debugger.log(text)


def main():
    """Initialize the decompiler and decompile the function where the cursor is
    positioned. In case that the function memory address could not be obtained,
    return an error.

    """
    print "\n" * 20
    start = None

    try:
        point_source = PointSource()
        point_source.log("[+] Initiating decompilation process...")

        start = clock()

        point_source.set_screen_address_to_decompile()

        point_source.decompile()

    except PointSourceException, err:
        print "[-] Error : %s" % err

    finally:
        if start:
            end = clock()
            point_source.log("[!] Decompilation took %.2f seconds" % (end - start))

if __name__ in ["__main__"]:
    main()
