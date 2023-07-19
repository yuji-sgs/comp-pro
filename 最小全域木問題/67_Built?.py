"""
平面上に、N 個の街があります。
i 個目の街は、座標 (xi,yi) にあります。同じ座標に、複数の街があるかもしれません。
座標 (a,b) にある街と座標 (c,d) にある街の間に道を造るのには、
min(|a-c|,|b-d|) 円かかります。街と街の間以外に、道を造ることはできません。
任意の 2 つの街の間を、道を何本か通って行き来できるようにするためは、最低で何円必要でしょうか
"""
import heapq
N = int(input())
X = [] # ソートするためのリスト
Y = []
for n in range(N):
    x, y = map(int,input().split())
    X.append((x, n)) # 座標と街番号
    Y.append((y, n))
X.sort() # 座標でソート
Y.sort()
    
G = [[] for n in range(N)]
for n in range(N-1): # 数直線上で隣接している街と街の座標の差分を求める
    cost = X[n+1][0] - X[n][0]
    G[X[n+1][1]].append((cost, X[n][1])) # (辺のコスト, 行先)
    G[X[n][1]].append((cost, X[n+1][1]))
    
    cost = Y[n+1][0] - Y[n][0]
    G[Y[n+1][1]].append((cost, Y[n][1])) # (辺のコスト, 行先)
    G[Y[n][1]].append((cost, Y[n+1][1]))
    
visited = [0] * N
pq = []
for w, t in G[0]:
    heapq.heappush(pq, (w, t)) 
visited[0] = 1

ans = 0
while pq:
    w, t = heapq.heappop(pq)
    if visited[t] == 1:
        continue
    visited[t] = 1
    ans += w
    for w, s in G[t]:
        if visited[s] == 0:
            heapq.heappush(pq, (w, s))

print(ans)
