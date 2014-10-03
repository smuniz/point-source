# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc


class OutputMediaBaseException(Exception):
    """Generic exception for output media class."""
    pass


class OutputMediaBase(object):
    """Base class for all the outputting classes for every supported media."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_output(self, title):
        """Generate readble output in a new window."""
        return

    @abc.abstractmethod
    def create(self, title):
        """Create the new window with the specified title."""
        return

    @abc.abstractmethod
    def show(self):
        """Display the window inside the current application."""
        return
