from _test_common import *

assert copy.deepcopy(1) == 1
assert make_arr(3) == [0, 0, 0]

temp = make_arr(3, [0])
temp[0][0] = 1
assert temp == [[1], [0], [0]]


sys.stdin = io.StringIO("1 A")
assert input_list() == ["1", "A"]
sys.stdin = io.StringIO("1 A")
assert input_list([int, str]) == [1, "A"]
sys.stdin = io.StringIO("1 A")

sys.stdin = io.StringIO("1 A")
assert input_tuple() == ("1", "A")
sys.stdin = io.StringIO("1 A")
assert input_tuple([int, str]) == (1, "A")

sys.stdin = io.StringIO("1 2")
assert input_tuple(int) == (1, 2)

assert check_sub_str("BC", "ABCDE") == True
assert check_sub_str("AD", "ABCDE") == False
assert check_sub_str("AC", "ABCDE") == False
