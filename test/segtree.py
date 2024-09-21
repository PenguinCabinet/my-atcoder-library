import atcoder
import atcoder.segtree
import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))
from main import *


tree = atcoder.segtree.SegTree(lambda a, b: a + b, 0, [1, 2, 3, 4])
assert tree.prod(0, 2) == 3
assert tree.prod(1, 3) == 5

assert tree.get(1) == 2
tree.set(1, 5)
assert tree.get(1) == 5
assert tree.prod(0, 2) == 6

tree = atcoder.segtree.SegTree(max, -INF, [1, 2, 3, 4])
assert tree.prod(0, 3) == 3
