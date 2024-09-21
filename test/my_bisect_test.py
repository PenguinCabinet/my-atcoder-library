import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))
from my_bisect import *

test_data = [1, 3, 5]
assert bisect_index(test_data, 3) == 1
assert bisect_index(test_data, 4) is None

assert bisect_find_lt(test_data, 4) == 1
assert bisect_find_lt(test_data, 3) == 0
assert bisect_find_lt(test_data, 1) is None

assert bisect_find_le(test_data, 3) == 1
assert bisect_find_lt(test_data, 2) == 0
assert bisect_find_le(test_data, 1) == 0
assert bisect_find_le(test_data, 0) is None

assert bisect_find_gt(test_data, 4) == 2
assert bisect_find_gt(test_data, 3) == 2
assert bisect_find_gt(test_data, 2) == 1
assert bisect_find_gt(test_data, 1) == 1
assert bisect_find_gt(test_data, 0) == 0
assert bisect_find_gt(test_data, 5) is None

assert bisect_find_ge(test_data, 4) == 2
assert bisect_find_ge(test_data, 3) == 1
assert bisect_find_ge(test_data, 1) == 0
assert bisect_find_ge(test_data, 0) == 0
assert bisect_find_ge(test_data, 6) is None
