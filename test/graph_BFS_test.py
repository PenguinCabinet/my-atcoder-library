from _test_common import *

G = graph_t(8)
G.add(0, 1, 1)

G.add(1, 2, 1)
G.add(1, 3, 1)

G.add(2, 1, 1)

G.add(2, 4, 1)
G.add(2, 5, 1)
G.add(3, 6, 1)
G.add(3, 7, 1)


BFS_test_nodes_index = 0
BFS_test_nodes = [0, 1, 2, 3, 4, 5, 6, 7]


def node_func(node):
    global BFS_test_nodes_index
    assert node == BFS_test_nodes[BFS_test_nodes_index]
    BFS_test_nodes_index += 1


BFS(0, G, node_func, None)
