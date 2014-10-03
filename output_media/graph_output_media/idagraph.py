# 
# Copyright (c) 2013 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from idaapi import GraphViewer

class MyGraph(GraphViewer):
    def __init__(self, funcname, result):
        GraphViewer.__init__(self, "call graph of " + funcname)
        self.funcname = funcname
        self.result = result

    def OnRefresh(self):
        self.Clear()
        id = self.AddNode(self.funcname)
        for x in self.result.keys():
            callee = self.AddNode(x)
            self.AddEdge(id, callee)

        return True

    def OnGetText(self, node_id):
        return str(self[node_id])

