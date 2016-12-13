# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
from traceback import format_exc
from output_media.output_media_base import OutputMediaBase

try:
    import idaapi
except ImportError, err:
    raise OutputMediaBaseException("TextOutputMedia only available under IDA")


class GraphOutputMediaException(Exception):
    pass


class GraphOutputMedia(OutputMediaBase, idaapi.GraphViewer):
    """
    Given the IR code, transform it into a C/C++ readable code, display it
    appropiately and perform callbacks if applicable.
    """

    def __init__(self, ir):
        OutputMediaBase.__init__(self)
        idaapi.GraphViewer.__init__(self, "Function Graph")
        self.ir = ir

    def OnRefresh(self):
        idaapi.GraphViewer.OnRefresh(self)

        try:
            line = 0
            nodes = dict()

            for block in self.ir:

                instructions_block = list()

                #if block.hasLabel():
                #    instructions_block.append("%s\n\n" % block.getLabel()

                #if self.ir.getBlockIndex(block) == 0:
                #    instructions_block.append(self.generateFunctionOpening()

                #for stmt in block:
                for inst in block:

                    inst_line = ""
                    #if stmt.wasRemoved():
                    #    continue

                    #inst = stmt.get()
                    #if isinstance(inst, GotoStatement):
                    #    continue

                    str_address = "%08X:%03X" % (inst.address, line)
                    str_address = \
                        idaapi.COLSTR(str_address, idaapi.SCOLOR_ASMDIR)

                    str_inst = \
                        idaapi.COLSTR(str(inst), idaapi.SCOLOR_INSN)

                    instructions_block.append(
                        "%(str_address)s %(str_inst)s" % vars())
                    line += 1

                nodes[block] = self.AddNode("\n".join(instructions_block))

            for idx, bb in enumerate(self.ir):
                for succ in bb.successors():
                    node_a = nodes[bb]
                    node_b = nodes[succ]
                    #print "Adding %s ---> %s" % (node_a, node_b)
                    self.AddEdge(node_a, node_b)

        except Exception, err:
            if self.debug:
                print format_exc()

        return True

    def OnGetText(self, node_id):
        return str(self[node_id])

    def generate_output(self, title):
        """Generate graph output in a new IDA view window."""
        self.title = title

        crea = self.create()

        if not crea:
            self.clear()
            #self.add_line("hola manola")
            #self.show()
        else:
            #print "1 OK..."
            pass

        self.show()

        #self.cmd_id = self.AddCommand("matanga", "r")
        #print "----->", self.cmd_id
        return True

    def close(self):
        """Close the current window."""
        self.Close()

    def create(self):
        """Create the new window with the specified title."""
        #if not self.Create(self.title):
        #    #raise TextOutputMediaException("Unable to create custom viewer")
        #    return False
        #return True
        return False

    def clear(self):
        """Clear the window content."""
        self.Clear()

    def show(self):
        """Display the window inside the current application."""
        self.Show()

    def OnCommand(self, cmd_id):
        """
        Triggered when a menu command is selected through the menu or its hotkey
        """
        print "command:", cmd_id

    def OnClick(self, node_id):
        print "clicked on node %d" % node_id

    def OnSelect(self, node_id):
        """Triggered when a node is being selected

        @return: Return True to allow the node to be selected or False to disallow node selection change
        """
        # allow selection change
        print "selected node", node_id
        return True
