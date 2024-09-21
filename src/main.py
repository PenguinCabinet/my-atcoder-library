import sys
import itertools
import bisect
import math
import collections
import heapq
import atcoder
import copy

sys.setrecursionlimit(3 * (10**8))
INF = 1 << 63


def make_arr(N, elem=0):
    return [copy.deepcopy(elem) for i in range(N)]


def mmap(func, v):
    return list(map(func, v))


def input_tuple(func=str):
    return tuple(input_list(func))


def input_list(func=str):
    result = list(input().split())
    if isinstance(func, list):
        result = [func[i](e) for i, e in enumerate(result)]
    else:
        result = [func(e) for i, e in enumerate(result)]
    return result


def input_lists_int(N):
    ret = []
    for _ in range(N):
        ret.append(list(map(int, input().split())))
    ret = [[ret[j][i] for j in range(N)] for i in range(len(ret[0]))]

    return tuple(ret)


def YesNo(v):
    return "Yes" if v else "No"


def print_list(v):
    print(*v)


def check_sub_str(s1, s2):
    's1はs2の部分文字列か。s1="BC",s2="ABCDE"'
    return s1 in s2


def main():
    pass


main()
