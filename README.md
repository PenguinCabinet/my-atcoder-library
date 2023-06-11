# my-atcoder-library

# 二分探索
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
