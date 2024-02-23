# my-atcoder-library

## Atcoder-cliとonline-judge-toolsのチートシート

https://zenn.dev/penguincabinet/articles/9c05e423e4eaab

## 高速化チェック
- [ ] 連想配列ではなく配列を使えるところは配列を使う
- [ ] 配列の文字列の結合は`"".join` **ではなく** forループで足していく
- [ ] 極力、変換しない(例えば、listへ)。変換する場合はループの外で！
- [ ] 先頭への挿入・消去を高速(O(1))でやりたいなら、dequeをどうぞ
- [ ] 無限ループに入った時は、インデックスがループ中に、ちゃんと加算されているかチェック

## 再帰関数のリミット
再帰関数問題を解く場合。Pythonの再帰関数呼び出し制限に注意すること。
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

def main():
    pass

main()
```

## 二分探索
Kが配列Pに存在するか    
Iは、Kがある場所のインデックス
```
I=bisect.bisect_left(P,K)
if 0<=I and I<len(P):
    if P[I]==K:
        pass
```
配列Pにおける、**K以下の最大の数**がある場所のインデックス
```
I=bisect.bisect_left(P,K)
if 0<=I and I<len(P):
    pass
```
配列Pにおける、**K以上の最小の数**がある場所のインデックス
```
I=bisect.bisect_right(P,K)
if 0<=I and I<len(P):
    pass
```

## 幅優先探索
最短距離を幅優先探索で求めるもの
```python
from collections import deque
def search_func(node,deep):
    visited=set()
    Q=deque()
    Q.append(node)
    while len(Q)>0:
        temp=Q.popleft()
        #TODO ここに現在の探索node tempにする処理を書く
        visited.add(temp)
        for e in ab[temp]:
            if e in visited:
                continue
            Q.append(e)
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
