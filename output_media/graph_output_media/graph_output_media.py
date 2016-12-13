# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from output_media.output_media_base import OutputMediaBase

import idaapi


class GraphOutputMediaException(Exception):
    pass


class GraphOutputMedia(OutputMediaBase, idaapi.GraphViewer):
    """
    Given the IR code, transform it into a C/C++ readable code, display it
    appropiately and perform callbacks if applicable.
    """

    def __init__(self):
        OutputMediaBase.__init__(self)
        idaapi.GraphViewer.__init__(self, "Decompiled function call graph")

    def OnRefresh(self):
        self.Clear()

        try:
            line        = 0
            nodes       = dict()

            for block in self.ir:

                instructions_block = ""

                if block.hasLabel():
                    instructions_block += "%s\n\n" % block.getLabel()

                if self.ir.getBlockIndex(block) == 0:
                    instructions_block += self.generateFunctionOpening()

                for stmt in block:

                    if stmt.wasRemoved():
                        continue

                    inst = stmt.get()
                    if isinstance(inst, GotoStatement):
                        continue

                    line                += 1
                    instructions_block  += "%(line)2d: %(inst)s;\n" % vars()

                nodes[block] = self.AddNode(instructions_block)

            for block_key in nodes:
                for edge in block_key.getInEdges():
                    self.AddEdge(edge, nodes[block_key])

        except Exception, err:
            from traceback      import format_exc
            print format_exc() + "\n"
            pass

        return True

    def OnGetText(self, node_id):
        return str(self[node_id])

    def generate_output(self):
        """
        Generate C-like readble output in a graph window.
        """
        #self._title = "Call graph of %s" % self.getMir().getName()
        self.Show()
        #self.cmd_id = self.AddCommand("matanga", "r")
        #print "----->", self.cmd_id
        return True

    def OnCommand(self, cmd_id):
        """
        Triggered when a menu command is selected through the menu or its hotkey
        """
        print "command:", cmd_id

    def OnClick(self, node_id):
        print "clicked on", self[node_id]

    def OnSelect(self, node_id):
        """
        Triggered when a node is being selected
        @return: Return True to allow the node to be selected or False to disallow node selection change
        """
        # allow selection change
        print "selected node", node_id
        return True

    def generateFunctionOpening(self):

        ret_type    = self.ir.getReturnType()
        call_conv   = self.ir.getCallingConvention()
        func_name   = self.ir.getName()
        params      = ",".join( \
                        [" ".join(param) for param in self.ir.getParamter()])

        func_opening  = "%(ret_type)s %(call_conv)s %(func_name)s ( %(params)s)\n\n"
        func_opening %= vars()

        return func_opening

