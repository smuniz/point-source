# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#
import abc

from traceback import format_exc
from output_media.graph_output_media import GraphOutputMedia, \
    GraphOutputMediaException


class BasicBlockGraphOutputException(GraphOutputMediaException):
    """Generic exception for graph output media exception."""
    pass


class BasicBlockGraphOutput(GraphOutputMedia):
    """Display a graph view of the basic blocks (and their corresponding
    instructions) that compuse the function being analyzed by its LIR.
    
    """

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
                #for succ in bb.predecessors():
                    node_a = nodes[bb]
                    node_b = nodes[succ]
                    #print "Adding %s ---> %s" % (node_a, node_b)
                    self.add_edge(node_a, node_b)

        except Exception, err:
            if self.debug:
                print format_exc()

        return True

