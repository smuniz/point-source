# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class SimpleGraphException(Exception):
    """Simple graph class generic exception."""
    pass


class SimpleGraph(object):
    """Simple graph storage class."""

    def __init__(self, in_edges=None, out_edges=None):
        """Initialize instance."""
        # Populate the in edge list is a list is specified.
        if in_edges:
            self.in_edges = in_edges
        else:
            # Otherwise create it empty.
            self.in_edges = list()

        # Populate the out edge list is a list is specified.
        if out_edges:
            self.out_edges = out_edges
        else:
            # Otherwise create it empty.
            self.out_edges = list()

    def add_out_edge(self, edge):
        """Add an out edge."""
        self.out_edges.append(edge)

    def get_out_edge(self, n):
        """Return the a specific out edge."""
        return self.out_edges[n]

    def get_out_edges(self):
        """Return the list of out edges."""
        return self.out_edges

    def add_in_edge(self, edge):
        """Add an in edge."""
        self.in_edges.append(edge)

    def get_in_edge(self, n):
        """Return the a specific in edge."""
        return self.in_edges[n]

    def get_in_edges(self):
        """Return the list of in edges."""
        return self.in_edges

