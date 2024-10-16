from _test_common import *

assert graph_edge_t(2, 1).__str__() == "To_node:2 W:1"
assert graph_edge_t(2, 1) == graph_edge_t(2, 1)

G = graph_t(3)
G.add(0, 1, 1)
G.add(1, 2, 1)
G.add(2, 1, 1)

assert G.list_edges(0) == [graph_edge_t(1, 1)]
assert G.list_edges(1) == [graph_edge_t(2, 1)]
assert G.list_edges(2) == [graph_edge_t(1, 1)]
