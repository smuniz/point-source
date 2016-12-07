# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class MultiDiGraphException(Exception):
    """Simple graph class generic exception."""
    pass


#class Node(object):
#    """..."""
#
#    def __init__(self, in_edges=list(), out_edges=list()):
#        """Initialize instance."""
#        # Populate the in-edge list if a list is specified.
#        self.in_edges = in_edges
#
#        # Populate the out-edge list if a list is specified.
#        self.out_edges = out_edges
#
#    def add_out_edge(self, edge):
#        """Add an out edge."""
#        self.out_edges.append(edge)
#
#    def get_out_edge(self, n):
#        """Return the a specific out edge."""
#        return self.out_edges[n]
#
#    def get_out_edges(self):
#        """Return the list of out edges."""
#        return self.out_edges
#
#    def add_in_edge(self, edge):
#        """Add an in edge."""
#        self.in_edges.append(edge)
#
#    def get_in_edge(self, n):
#        """Return the a specific in edge."""
#        return self.in_edges[n]
#
#    def get_in_edges(self):
#        """Return the list of in edges."""
#        return self.in_edges


class MultiDiGraph(object):
    """Simple graph storage class."""
    def __init__(self):
        pass

    def add_node(self, n, attr_dict):
        """Add a single node n and update node attributes."""
        pass

    def add_nodes_from(self, nodes, **attr):
        """Add multiple nodes."""
        pass

    def remove_node(self, n):
        """Remove node n."""
        pass

    def remove_nodes_from(self, nodes):
        """Remove multiple nodes."""
        pass

    def add_edge(self, u, v, key, attr_dict):
        """Add an edge between u and v."""
        pass

    def add_edges_from(self, ebunch, attr_dict):
        """Add all the edges in ebunch."""
        pass

    #def add_weighted_edges_from(self, ebunch, ...):
    #    """Add all the edges in ebunch as weighted edges with specified weights."""
    #    pass

    def remove_edge(self, u, v, key):
        """Remove an edge between u and v."""
        pass

    def remove_edges_from(self, ebunch):
        """Remove all dges specified in ebunch."""
        pass

    def add_star(self, nodes, **attr):
        """Add a star."""
        pass

    def add_path(self, nodes, **attr):
        """Add a path."""
        pass

    def add_cycle(self, nodes, **attr):
        """Add a cycle."""
        pass

    def clear(self):
        "Remove all nodes and edges from the graph."""
        pass

