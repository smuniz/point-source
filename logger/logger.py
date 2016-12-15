#!/usr/bin/env python
# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part Binary Scope disassembler
#
"""

The Logger is a class for logging script information to the specified output
device/media.

"""
__author__      = "Sebastian Muniz"
__year__        = "2013"
__version__     = "1.0"
__nonsense__    = "This script is part of Binary Scope"


class Logger(object):
    """Perform all logging related operations."""

    #
    # This code is under development. Although it's being used in the project it's
    # incomplete (functional, but incomplete).
    #
    # It'll be enhanced on future versions as it's needed but for the moment it'll
    # remain as is.
    #
    # TODO : Add python standard logging module.

    ALL = 0
    DEBUG = 1
    INFO = 2
    ERROR = 3
    CRITICAL = 4
    NONE = 5

    def __init__(self, output=None, level=INFO):
        self.output_redirector = output
        self.level = level

    @property
    def level(self):
        """Return the logging threshold."""
        return self._level

    @level.setter
    def level(self, level):
        """Store the new logging threshold."""
        self._level = level

    @property
    def output_redirector(self):
        """Return the previously specify a file-like trace object."""
        return self._output_handler

    @output_redirector.setter
    def output_redirector(self, output_handler):
        """Specify a file-like object invoked to trace class output."""
        self._output_handler = output_handler

    def critical(self, line):
        """Output a critical error line to the logging device."""
        self.__trace("[CRT] %s\n" % line, self.CRITICAL)

    def error(self, line):
        """Output an error line to the logging device."""
        self.__trace("[ERR] %s\n" % line, self.ERROR)

    def debug(self, line):
        """Output a debug line to the logging device."""
        self.__trace("[DBG] %s\n" % line, self.DEBUG)

    def info(self, line):
        """Output an information line to the logging device."""
        self.__trace("[INF] %s\n" % line, self.INFO)

    def __trace(self, output, level):
        """Output the specified buffer content to the logging device."""
        if self.output_redirector is not None and level >= self.level:
            self.output_redirector.write(output)
