# my-atcoder-library

- [my-atcoder-library](#my-atcoder-library)
  - [Atcoder-cliとonline-judge-toolsのチートシート](#atcoder-cliとonline-judge-toolsのチートシート)
    - [①コンテストをローカルにクローン](#コンテストをローカルにクローン)
    - [⑤テストケースの検証](#テストケースの検証)
  - [テンプレ](#テンプレ)
  - [スペースに分けて、配列を一行で表示](#スペースに分けて配列を一行で表示)
  - [順序付きソート](#順序付きソート)
  - [二分探索](#二分探索)
    - [関数に対する二分探索](#関数に対する二分探索)
  - [部分文字列(部分列)](#部分文字列部分列)
  - [優先度付きキュー](#優先度付きキュー)
  - [グラフ](#グラフ)
    - [幅優先探索](#幅優先探索)
    - [ダイクストラ法](#ダイクストラ法)
    - [UnionFind](#unionfind)
    - [最大フロー問題](#最大フロー問題)
  - [累積和](#累積和)
    - [0を含めない場合](#0を含めない場合)
    - [0を含める場合](#0を含める場合)
  - [素数列挙](#素数列挙)
  - [セグメント木](#セグメント木)


## Atcoder-cliとonline-judge-toolsのチートシート

https://zenn.dev/penguincabinet/articles/9c05e423e4eaab

### ①コンテストをローカルにクローン
```bash
acc new abcN
```

### ⑤テストケースの検証
```bash
oj t -c "python main.py" -d ./tests/
```

## テンプレ
[main.py](src/main.py)

## スペースに分けて、配列を一行で表示
```python
print_list(Ans)
```

## 順序付きソート
[SortedSet.py](src/SortedSet.py)


## 二分探索
```python
bisect_index(arr,x)
bisect_find_lt(arr,x)
```


### 関数に対する二分探索

```python
    L=1
    R=100000000
    m=0
    while L<R:
        m=(L+R)//2
        temp=check(m)
        if temp>=K:
            R=m
        else:
            L=m+1
    print(L)
```

## 部分文字列(部分列)

例
```python
s1="AC"
s2="ABCDE"
#False

s1="AB"
s2="ABCDE"
#True
```

```python
check_sub_str(s1,s2)
```

## 優先度付きキュー
最小値から取り出す。
```python
a = [1,6,8,0,-1]
heapq.heapify(a)
heapq.heappop(a)
heapq.heappush(a,-2)
```

最大値から取り出す。
```python

def heapify_max(a):
    for i in range(len(a)):
        a*=-1
    heapq.heapify(a)

def heappop_max(a):
    return -heapq.heappop(a)

def heappush_max(a,x):
    return heapq.heappush(a,-2)

a = [1,6,8,0,-1]
heapq.heapify(a)
heapq.heappop(a)
heapq.heappush(a,-2)
```



## グラフ

### 幅優先探索
最短距離を幅優先探索で求めるもの
```python
def BFS(node,G):
    visited=set()
    Q=collections.deque()
    Q.append([node,0])
    while len(Q)>0:
        temp,dist=Q.popleft()
        #TODO ここに現在の探索node tempにする処理を書く
        visited.add(temp)
        for e in G[temp]:
            if e in visited:
                continue
            Q.append([e,dist+1])
```

### ダイクストラ法
重み付き有向グラフの最短経路を求める。node 1からスタート
```python
def Dijkstra_search_func(N,G):
    decided=[False for i in range(N+1)]
    cur=[INF for i in range(N+1)]
    back=[-1 for i in range(N+1)]

    cur[-1]=0

    Q=[]
    back[-1]=-1
    heapq.heappush(Q,(cur[-1],N))
    while len(Q)>0:
        _,pos=heapq.heappop(Q)
        if decided[pos]:
            continue
        decided[pos]=True

        for g in G[pos]:
            next_data,cost=tuple(g)
            if cur[next_data]>cur[pos]+cost:
                cur[next_data]=cur[pos]+cost
                back[next_data]=pos
                heapq.heappush(Q,(cur[next_data],next_data))
    root=[1]
    while root[-1]!=N:
        root.append(back[root[-1]])

    return cur,root
```

使用例
```python
    N,M=tuple(map(int,input().split()))
    G=[[] for i in range(N+1)]
    for i in range(M):
        A,B,C=tuple(map(int,input().split()))
        G[A].append([B,C])
        G[B].append([A,C])
    A=Dijkstra_search_func(N,G)
```

### UnionFind

```python
class Union_Find:
    def __init__(self,N) -> None:
        self.roots=[i for i in range(N+1)]
        self.ranks=[1 for i in range(N+1)]
    
    def find(self,x):
        if x!=self.roots[x]:
            self.roots[x]=self.find(self.roots[x])
        return self.roots[x]
    def unite(self,x,y):
        tempx=self.find(x)
        tempy=self.find(y)
        if tempx==tempy:
            return
        
        if self.ranks[tempx]>self.ranks[tempy]:
            self.roots[tempy]=tempx
        elif self.ranks[tempx]<self.ranks[tempy]:
            self.roots[tempx]=tempy
        else:
            self.roots[tempy]=tempx
            self.ranks[tempx]+=1
    def same(self,x,y):
        return self.find(x)==self.find(y)
```

### 最大フロー問題
```python
def dfs(pos,goal,F:int,G,visited:set):
    if pos==goal:
        return F
    visited.add(pos)
    for e in G[pos]:
        if e.to in visited:
            continue
        if e.dist==0:
            continue
        Flow=dfs(e.to,goal,min(F,e.dist),G,visited)
        if Flow>=1:
            e.dist-=Flow
            G[e.to][e.rev].dist+=Flow
            return Flow

    return 0

def max_flow(start_data,end_data,G):
    Ans=0
    while True:
        ret=dfs(start_data,end_data,INF,G,set())
        if ret==0:
            break
        Ans+=ret
    return Ans

```


## 累積和
### 0を含めない場合
```python
sub_sum=list(itertools.accumulate(diff))
```
### 0を含める場合
```python
sub_sum=[0]+list(itertools.accumulate(diff))
```

## 素数列挙
```python
def Get_IsPrime_list(n):
    A=[True for i in range(n+1)]
    A[0]=False
    A[1]=False

    for i in range(2,n+1):
        if A[i]==True:
            temp=i*2
            while temp<=n:
                A[temp]=False
                temp+=i

    return A
```

## セグメント木
* posのインデックスは1から始まり、Nで終わる。nを含める！rangeでループする場合は、range(1,N+1)でやる
* l以上、r未満の範囲の特定の値を求める。**l以上、r以下を求めたい場合は`tree.prod(l, r+1)`で求める**

```python
tree = atcoder.segtree.SegTree(max, -INF, [1, 2, 3, 4])

tree.prod(0, 2)
tree.set(0,1)
tree.get(0)
```

* l以上、r未満の範囲の**最大値**を求める
* posのインデックスは1から始まり、Nで終わる。
```python
tree = atcoder.segtree.SegTree(max, -INF, [1, 2, 3, 4])
```

* l以上、r未満の範囲の**合計値**を求める
* posのインデックスは1から始まり、Nで終わる。
```python
tree = atcoder.segtree.SegTree(lambda a, b: a + b, 0, [1, 2, 3, 4])
```
