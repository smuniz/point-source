# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#
__all__ = ["SymbolsManager", "SymbolsManagerException"]


class Symbol(object):
    __slots__ = ["name", "type", "scope", "item"]

    def __init__(self, name, _type, scope, item):
        self.name = name
        self.type = _type
        self.scope = scope
        self.item = item


class SymbolsTable(object):
    """Store all the symbols that belong to a specific function."""

    def __init__(self, *args, **kw):
        #super(SymbolsTable,self).__init__(*args, **kw)
        #self.itemlist = super(SymbolsTable,self).keys()
        self.symbols = dict()
        self.variables = dict()

    def add_local_variable(self, address, name, item):
        """Add a new loscal variable to the symbols table."""
        self.variables[address] = Symbol(name, None, None, item)

    def add_symbol(self, address, name, _type, scope, item):
        """Add a regular symbol with its corresponding information to the
        symbols table.
        
        """
        self.symbols[address] = Symbol(name, _type, scope, item)

    def __str__(self):
        _str = ["[+] Local variables list:", ]
        for k, (addr, i) in enumerate(self.variables.iteritems()):
            _str.append("\t%02d | %08x | %10s | %10s | %10s | %r" % (
                k, addr, i.name, i.type, i.scope, i.item))
            
        _str.append("[+] Symbols mapping list:")
        for k, (addr, i) in enumerate(self.symbols.iteritems()):
            _str.append("\t%02d | %08x | %10s | %10s | %10s | %r" % (
                k, addr, i.name, i.type, i.scope, i.item))

        return "\n".join(_str)
                

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
        if type(address) not in (int, long):
            raise SymbolsManagerException(
                "Invalid symbol address specified (%r)" % address)

        return self._functions_symbols.setdefault(address, SymbolsTable())
