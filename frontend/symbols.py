# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from collections import MutableMapping

__all__ = ["SymbolsManager", "SymbolsManagerException"]


class Symbol(object):
    __slots__ = ["name", "type", "scope"]

    def __init__(self, name, _type, scope):
        self.name = name
        self.type = _type
        self.scope = scope


class SymbolsTable(dict):
    """Store all the symbols that belong to a specific function."""

    def __init__(self, *args, **kw):
        super(SymbolsTable,self).__init__(*args, **kw)
        self.itemlist = super(SymbolsTable,self).keys()

    def __getitem__(self, key):
        return super(SymbolsTable, self).__getitem__(key)

    def __setitem__(self, key, value):
         # TODO: what should happen to the order if
         #       the key is already in the dict       
        self.itemlist.append(key)
        super(SymbolsTable,self).__setitem__(key, value)

    def __iter__(self):
        return iter(self.itemlist)

    def keys(self):
        return self.itemlist

    def values(self):
        return [self[key] for key in self]  

    def itervalues(self):
        return (self[key] for key in self)


class SymbolsManagerException(Exception):
    """Generic exception class for symbols manager."""
    pass


class SymbolsManager(object):
    """Symbol storage for all the module defined symbols found during the
    analysis and also containing user-defined information.

    This class contains multiple symbol tables, one for each function defined
    and also additional tables for global variables.
    """

    def __init__(self):
        self.functions_symbols = dict() # key = address | value = symbol table
        self.global_symbols = dict() # key = address | value = symbol table

    @property
    def global_symbols(self):
        """Return a dictionary with all the global symbols."""
        return self._global_symbols

    @global_symbols.setter
    def global_symbols(self, tables):
        """Store a dictionary of all the global symbols."""
        self._global_symbols = tables

    @property
    def functions_symbols(self):
        """Return a dictionary of all the symbols tables ordered by its
        addresses in the binary under analysis.

        """
        return self._functions_symbols

    @functions_symbols.setter
    def functions_symbols(self, symbols):
        """Store a dictionary of all the symbols tables."""
        self._functions_symbols = symbols

    def symbols(self, address):
        """Return the of symbols for the given address."""
        if type(address) is not int:
            raise SymbolsManagerException(
                "Invalid symbol address specified (%r)" % address)

        return self._functions_symbols.setdefault(address, SymbolsTable())
