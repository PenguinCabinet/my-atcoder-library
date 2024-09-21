import bisect


# Function details by https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
def bisect_index(a, x):
    "Locate the leftmost value exactly equal to x"
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


def bisect_find_lt(a, x):
    "Find the largest element < x, or None if it doesn't exist"
    i = bisect.bisect_left(a, x)
    if i:
        return i - 1
    return None


def bisect_find_le(a, x):
    "Find the largest element <= x, or None if it doesn't exist."
    i = bisect.bisect_right(a, x)
    if i:
        return i - 1
    return None


def bisect_find_gt(a, x):
    "Find the smallest element > x, or None if it doesn't exist."
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return i
    return None


def bisect_find_ge(a, x):
    "Find the smallest element >= x, or None if it doesn't exist."
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    return None
