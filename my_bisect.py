import bisect  
def my_bisect_index(A:list[int],op:str,X:int):
    def index(a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return None

    def find_lt(a, x):
        'Find rightmost value less than x'
        i = bisect.bisect_left(a, x)
        if i:
            return i-1
        return None

    def find_le(a, x):
        'Find rightmost value less than or equal to x'
        i = bisect.bisect_right(a, x)
        if i:
            return i-1
        return None

    def find_gt(a, x):
        'Find leftmost value greater than x'
        i = bisect.bisect_right(a, x)
        if i != len(a):
            return i
        return None

    def find_ge(a, x):
        'Find leftmost item greater than or equal to x'
        i = bisect.bisect_left(a, x)
        if i != len(a):
            return i
        return None
    
    if op=="==":
        return index(A,X)
    elif op=="<":
        return find_lt(A,X)
    elif op=="<=":
        return find_le(A,X)
    elif op==">":
        return find_gt(A,X)
    elif op==">=":
        return find_ge(A,X)
    else:
        raise ValueError

arr=[2, 2, 5, 7, 11, 13, 17, 19]

assert(my_bisect_index(arr,"==",11)==4)
assert(my_bisect_index(arr,"==",12) is None)
assert(my_bisect_index(arr,"==",20) is None)
assert(my_bisect_index(arr,"==",0) is None)
assert(my_bisect_index(arr,"==",2)==0)

print(my_bisect_index(arr,"<=",2))
assert(my_bisect_index(arr,"<=",2)==1)

assert(my_bisect_index(arr,"<",2) is None)
assert(my_bisect_index(arr,"<=",1) is None)

assert(my_bisect_index(arr,">=",11)==4)
assert(my_bisect_index(arr,">",11)==5)

assert(my_bisect_index(arr,">=",19)==7)
assert(my_bisect_index(arr,">=",20) is None)
assert(my_bisect_index(arr,">",19) is None)
