import sys
import itertools
import more_itertools
import bisect
import math
import collections
import heapq
import atcoder
import atcoder.segtree
from atcoder.modint import *
import copy
from typing import *
import string
from abc import ABC, abstractmethod

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


def input_lists(N, func=str):
    result = []
    for _ in range(N):
        if isinstance(func, list):
            result.append([func[i](e) for i, e in enumerate(input().split())])
        else:
            result.append([func(e) for i, e in enumerate(input().split())])
    result = [[result[j][i] for j in range(N)] for i in range(len(result[0]))]

    return tuple(result)


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


def bisect_index(a, x, key=lambda v: v, lo=0, hi=None):
    "Locate the leftmost value exactly equal to x"
    if hi is None:
        hi = len(a)
    i = bisect.bisect_left(a, x, key=key, lo=lo, hi=hi)
    if i != len(a) and key(a[i]) == x:
        return i
    return None


def bisect_find_lt(a, x, key=lambda v: v, lo=0, hi=None):
    "Get the index of the largest element < x, or None if it doesn't exist"
    if hi is None:
        hi = len(a)
    i = bisect.bisect_left(a, x, key=key, lo=lo, hi=hi)
    if i:
        result = i - 1
        if lo <= result and result < hi:
            return result
    return None


def bisect_find_le(a, x, key=lambda v: v, lo=0, hi=None):
    "Get the index of the largest element <= x, or None if it doesn't exist."
    if hi is None:
        hi = len(a)
    i = bisect.bisect_right(a, x, key=key, lo=lo, hi=hi)
    if i:
        result = i - 1
        if lo <= result and result < hi:
            return result
    return None


def bisect_find_gt(a, x, key=lambda v: v, lo=0, hi=None):
    "Get the index of the smallest element > x, or None if it doesn't exist."
    if hi is None:
        hi = len(a)
    i = bisect.bisect_right(a, x, key=key, lo=lo, hi=hi)
    if i != len(a):
        return i
    return None


def bisect_find_ge(a, x, key=lambda v: v, lo=0, hi=None):
    "Get the index of the smallest element >= x, or None if it doesn't exist."
    if hi is None:
        hi = len(a)
    i = bisect.bisect_left(a, x, key=key, lo=lo, hi=hi)
    if i != len(a):
        return i
    return None


def __bisect_func_find1(min_arg, max_arg, func, x):
    L = min_arg - 1
    R = max_arg
    m = 0
    while R - L > 1:
        m = (L + R) // 2

        result = func(m)

        if result >= x:
            R = m
        else:
            L = m
    return L, R


def bisect_func_find_ge(min_arg, max_arg, func, x):
    "Get the smallest result >= x."
    L, R = __bisect_func_find1(min_arg, max_arg, func, x)
    return R


def bisect_func_find_lt(min_arg, max_arg, func, x):
    "Get the largest result < x."
    L, R = __bisect_func_find1(min_arg, max_arg, func, x)
    return L


# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar("T")


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar("T")


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        n = self.size = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class graph_edge_t:
    def __init__(self, to_node: int, w: int, edge_id: int = 0):
        self.w = w
        self.to_node = to_node
        self.edge_id = edge_id

    def __eq__(self, value: int):
        return self.to_node == self.to_node and self.w == value.w

    def __str__(self):
        return f"To_node:{self.to_node} W:{self.w}"


class Base_graph_t(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def list_edges(self, from_node):
        pass


class graph_t(Base_graph_t):
    def __init__(self, N: int):
        self.G: dict[list[graph_edge_t]] = [[] for _ in range(N)]
        self.N: int = N
        self.edge_id_count: int = 0

    def add(
        self,
        from_node: int,
        to_node: Union[int, None] = None,
        w: int = 1,
        edge_id=None,
    ) -> None:
        if edge_id is None:
            edge_id = self.edge_id_count
            self.edge_id_count += 1
        if to_node is not None:
            self.G[from_node].append(
                graph_edge_t(
                    to_node,
                    w,
                    edge_id,
                )
            )

    def list_edges(self, from_node: int) -> list[graph_edge_t]:
        return self.G[from_node]


MapStr_to_graph_diagonal_move = [
    [(dy, dx) for dx in range(-1, 2) if not (dx == 0 and dy == 0)]
    for dy in range(-1, 2)
]
MapStr_to_graph_xy_move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class MapStr_graph_t(Base_graph_t):
    def __init__(self, S, H, W, allow_str, dyx):
        self.S = S
        self.H = H
        self.W = W
        self.dyx = dyx
        self.allow_str = allow_str

    def list_edges(self, from_node: int) -> list[graph_edge_t]:
        y, x = from_node
        result = []
        for dy, dx in self.dyx:
            if 0 <= y + dy and y + dy < self.H and 0 <= x + dx and x + dx < self.W:
                if self.S[y + dy][x + dx] in self.allow_str:
                    result.append(
                        graph_edge_t((y + dy, x + dx), 1, self.W * (y + dy) + x + dx)
                    )
        return result




def Dijkstra(start_node, G):
    decided = [False for i in range(G.N)]
    dist = [INF for i in range(G.N)]

    dist[start_node] = 0

    Q = []
    heapq.heappush(Q, (dist[start_node], start_node))
    while len(Q) > 0:
        _, node = heapq.heappop(Q)
        if decided[node]:
            continue
        decided[node] = True

        for edge in G.list_edges(node):
            if dist[edge.to_node] > dist[node] + edge.w:
                dist[edge.to_node] = dist[node] + edge.w
                heapq.heappush(Q, (dist[edge.to_node], edge.to_node))

    return dist


def RunLengthEncoding(v: list[int]) -> list[list[int, int]]:
    result = []
    for e in itertools.groupby(v):
        result.append([e[0], len(list(e[1]))])
    return result


def Eratosthenes(n):
    isprime = [True for _ in range(n)]
    result = []
    isprime[0] = False
    isprime[1] = False
    for i in range(2, n):
        if isprime[i]:
            result.append(i)
            j = i * 2
            while j < n:
                isprime[j] = False
                j += i

    return result


def main():
    pass


main()
