# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class Graph(object):
    """Simple graph storage class."""

    def __init__(self, in_edges=None, out_edges=None):
        if in_edges is not None:
            self.in_edges = in_edges
        else:
            self.in_edges = list()
        if out_edges is not None:
            self.out_edges = out_edges
        else:
            self.out_edges = list()

    def add_out_edge(self, edge):
        self.out_edges.append(edge)

    def get_out_edge(self, n):
        return self.out_edges[n]

    def get_out_edges(self):
        return self.out_edges

    def add_in_edge(self, edge):
        #print "---> got in edge %r" % edge
        self.in_edges.append(edge)

    def get_in_edge(self, n):
        return self.in_edges[n]

    def get_in_edges(self):
        return self.in_edges
