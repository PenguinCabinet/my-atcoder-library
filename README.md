# my-atcoder-library

- [my-atcoder-library](#my-atcoder-library)
  - [Atcoder-cliとonline-judge-toolsのチートシート](#atcoder-cliとonline-judge-toolsのチートシート)
    - [①コンテストをローカルにクローン](#コンテストをローカルにクローン)
    - [⑤テストケースの検証](#テストケースの検証)
  - [テンプレ](#テンプレ)
  - [スペースに分けて、配列を一行で表示](#スペースに分けて配列を一行で表示)
  - [二分探索](#二分探索)
    - [探索したい数値以下のうち最大の数値を探索](#探索したい数値以下のうち最大の数値を探索)
    - [探索したい数値未満のうち最大の数値を探索](#探索したい数値未満のうち最大の数値を探索)
    - [探索したい数値以上のうち最小の数値を探索](#探索したい数値以上のうち最小の数値を探索)
    - [探索したい数値を超えるもののうち最小の数値を探索](#探索したい数値を超えるもののうち最小の数値を探索)
    - [関数に対する二分探索](#関数に対する二分探索)
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
```
acc new abcN
```

### ⑤テストケースの検証
```
oj t -c "python main.py" -d ./tests/
```

## テンプレ
```python
#int(input())
#list(input())
#list(map(int,input().split()))
#tuple(map(int,input().split()))
#tuple(input().split())
import sys
import itertools
import bisect
import math
import collections
import heapq
sys.setrecursionlimit(3*(10**8))
INF=1<<61

def make_arr(N,elem=0):
    return [elem for i in range(N)]

def input_tuple_int():
    return tuple(map(int,input().split()))
def input_tuple():
    return tuple(input().split())

def input_list_int():
    return list(map(int,input().split()))

def input_lists_int(N):
    ret=[]
    for _ in range(N):
        ret.append(list(map(int,input().split())))
    ret=[[ret[j][i] for j in range(N)] for i in range(len(ret[0]))]

    return tuple(ret)

class Graph_Edge_t:
    def __init__(self,to,dist,rev):
        self.to = to
        self.dist=dist
        self.rev = rev

def Conv_graph_list_base(Nodes_len,from_list,to_list,dists=None,directed=True,Add_rev=False,residual=False):
    if len(from_list)!=len(to_list):
        raise ValueError
    G=[[] for i in range(Nodes_len+1)]
    for i in range(len(from_list)):
        
        dist=dists[i] if dists is not None else None
        temp_to=Graph_Edge_t(to_list[i],dist,len(G[to_list[i]]) if Add_rev else None)
        temp_from=Graph_Edge_t(from_list[i],dist if not residual else 0,len(G[from_list[i]]) if Add_rev else None)

        G[from_list[i]].append(temp_to)
        if not directed:
            G[to_list[i]].append(temp_from)

    return G
def Conv_graph_list(Nodes_len,from_list,to_list,dists,directed=False):
    return Conv_graph_list_base(Nodes_len,from_list,to_list,dists,directed=directed,residual=False,Add_rev=False)

def Conv_graph_list_residual(Nodes_len,from_list,to_list,dists):
    return Conv_graph_list_base(Nodes_len,from_list,to_list,dists,directed=False,residual=True,Add_rev=True)

def YesNo(v):
    return "Yes" if v else "No"

def main():
    pass

main()
```

## スペースに分けて、配列を一行で表示
```python
print(*Ans)
```

## 二分探索

条件に該当するものが存在した場合、インデックスを返す

存在しない場合、Noneを返す。

```python
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
```

### 探索したい数値以下のうち最大の数値を探索

```python
my_bisect_index(arr,"<=",2)
```

### 探索したい数値未満のうち最大の数値を探索

```python
my_bisect_index(arr,"<",2)
```

### 探索したい数値以上のうち最小の数値を探索

```python
my_bisect_index(arr,">=",2)
```

### 探索したい数値を超えるもののうち最小の数値を探索
```python
my_bisect_index(arr,">",2)
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

## グラフ

### 幅優先探索
最短距離を幅優先探索で求めるもの
```python
def search_func(node,G):
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
```
sub_sum=itertools.accumulate(diff)
```
### 0を含める場合
```
sub_sum=[0]+itertools.accumulate(diff)
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
* l以上、r未満の範囲の特定の値を求める。**l以上、r以下を求めたい場合は`Query(l,r+1)`で求める**

詳しい使い方はスクロール
```python
class SegTree:
    def __init__(self,N,func,init_elem=0) -> None:
        self.size=1
        while self.size<N:
            self.size*=2
        self.init_elem=init_elem
        self.data=[self.init_elem for i in range(2*self.size+1)]
        self.func=func
        self.N=N
    
    def Update(self,pos,x):
        temp_pos=pos+self.size-1
        self.data[temp_pos]=x
        while temp_pos>=2:
            temp_pos//=2
            self.data[temp_pos]=self.func(self.data[2*temp_pos],self.data[2*temp_pos+1]) 

    def Query(self,l,r,a=None,b=None,u=1):
        if a is None:
            a=1
        if b is None:
            b=self.size+1
            
        if r<=a or b<=l:
            return self.init_elem
        if l<=a and b<=r:
            return self.data[u]

        m=(a+b)//2
        temp1=self.Query(l,r,a,m,2*u)
        temp2=self.Query(l,r,m,b,2*u+1)

        return self.func(temp1,temp2)

    def Get_nodes_arr(self) -> str:
        return self.data[self.size:self.size+self.N]
```

* l以上、r未満の範囲の**最大値**を求める
* posのインデックスは1から始まり、Nで終わる。
```python
seg_tree=SegTree(N,max,init_elem=-1*(10**10))
```

* l以上、r未満の範囲の**合計値**を求める
* posのインデックスは1から始まり、Nで終わる。
```python
seg_tree=SegTree(N,lambda v1,v2:v1+v2,init_elem=0)
```
