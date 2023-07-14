"""
1 から N までの番号がついた N 個の頂点を持つ根付き木が与えられます。 
この木の根は頂点 1 で、i 番目の辺 (1≤i≤N-1) は頂点aiと頂点biを結びます。
各頂点にはカウンターが設置されており、はじめすべての頂点のカウンターの値は 0 です。
これから、以下のような Q 回の操作が行われます。
・操作j (1≤j≤Q): 頂点pjを根とする部分木に含まれるすべての頂点のカウンターの値にxjを足す。
すべての操作のあとの各頂点のカウンターの値を求めてください。
"""
import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
link = [[] for _ in range(N+1)]

# 隣接リストを作成
for n in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
    
V = [0] * (N+1) # 各ノードのカウンターを格納するリスト

for q in range(Q):
    p, x = map(int, input().split())
    V[p] += x # `操作`の際の根に当たるノードのカウンター`V`に先に値を加算する。

def dfs(i, parent, acc): # 深さ優先探索
    V[i] += acc # 親ノードまでの累積値を加算
    for j in link[i]:
        if j != parent: # 親ノードを追加しない
            dfs(j,i,V[i])
            
dfs(1, 0 , 0) # 親ノードを0としてスタート
V = [str(v) for v in V]
print (" ".join(V[1:])) # 1番目のノードは除く
