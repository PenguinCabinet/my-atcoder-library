# my-atcoder-library

## 再帰関数のリミット
再帰関数問題を解く場合。Pythonの再帰関数呼び出し制限に注意すること。
```python
import sys
sys.setrecursionlimit(3*(10**5))
```

## 二分探索
k以下のうち最大の要素のインデックスを返す。
```python
def bs_max(x,k):
    l=-1
    r=len(x)
    while r-l>1:
        m=l+(r-l)//2
        if x[m]<=k:
            l=m
        else:
            r=m
    return l
```

k以上のうち最小の要素のインデックスを返す。
```python
def bs_min(x,k):
    l=-1
    r=len(x)
    while r-l>1:
        m=l+(r-l)//2
        if x[m]>=k:
            r=m
        else:
            l=m
    return r
```

```python
def binary_search(x:list,k,cmp:function,key:function=lambda v,i:v[i]):
    ng=-1
    ok=len(x)
    while abs(ok-ng)>1:
        m=(ok+ng)//2
        if cmp(key(x,m),k):
            ok=m
        else:
            ng=m
    return ok
```

