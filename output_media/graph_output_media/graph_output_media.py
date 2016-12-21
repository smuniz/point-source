# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc

from traceback import format_exc
from output_media.output_media_base import OutputMediaBase, \
    OutputMediaBaseException

try:
    import idaapi
except ImportError, err:
    raise OutputMediaBaseException("Graph output only available under IDA Pro")


class GraphOutputMediaException(Exception):
    pass


class GraphOutputMedia(OutputMediaBase, idaapi.GraphViewer):
    """
    Given the IR code, transform it into a C/C++ readable code, display it
    appropiately and perform callbacks if applicable.
    """

    def __init__(self, title):
        self.debug = True
        OutputMediaBase.__init__(self)
        idaapi.GraphViewer.__init__(self, title)

    def OnRefresh(self):
        """Handle refresh event on the graph."""
        idaapi.GraphViewer.OnRefresh(self)

        # Invoke the children on_refresh() method to perform the necessary
        # changes to the graph.
        return self.on_refresh()

    @abc.abstractmethod
    def on_refresh(self):
        """Callback function invoked when the graph needs to be refreshed."""
        return

    def OnGetText(self, node_id):
        # TODO call childern method ????
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
        return True

    def close(self):
        """Close the current window."""
        self.Close()

    def create(self):
        """Create the new window with the specified title."""
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
        if self.debug:
            print "[DEBUG] Command :", cmd_id
        try:
            self.on_command(cmd_id)
        except AttributeError, err:
            if self.debug:
                print "[-] Error : %s" % err

    def OnClick(self, node_id):
        """Handle the Click event on the graph."""
        if self.debug:
            print "clicked on node %d" % node_id
        try:
            self.on_click(node_id)
        except AttributeError, err:
            if self.debug:
                print "[-] Error : %s" % err

    def OnSelect(self, node_id):
        """Triggered when a node is being selected

        @return: Return True to allow the node to be selected or False to disallow node selection change
        """
        # Allow selection change
        if self.debug:
            print "[DEBUG] selected node", node_id
        try:
            self.on_select(node_id)
        except AttributeError, err:
            if self.debug:
                print "[-] Error : %s" % err
        return True

    def add_node(self, node):
        """Add a new node to the graph."""
        return self.AddNode(node)

    def add_edge(self, node_a, node_b):
        """Add a new edge connecting the two specified nodes."""
        return self.AddEdge(node_a, node_b)

class BasicBlockGraphOutputException(GraphOutputMediaException):
    """Generic exception for graph output media exception."""
    pass


class BasicBlockGraphOutput(GraphOutputMedia):
    """..."""

    def __init__(self, ir):
        """Initialize the instance."""
        super(BasicBlockGraphOutput, self).__init__("Function Graph")
        self.ir = ir

    def on_refresh(self):
        """Callback function invoked when the graph needs to be refreshed."""
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

                nodes[block] = self.add_node("\n".join(instructions_block))

            for idx, bb in enumerate(self.ir):
                for succ in bb.successors():
                    node_a = nodes[bb]
                    node_b = nodes[succ]
                    #print "Adding %s ---> %s" % (node_a, node_b)
                    self.add_edge(node_a, node_b)

        except Exception, err:
            if self.debug:
                print format_exc()

        return True

