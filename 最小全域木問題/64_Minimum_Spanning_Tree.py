"""
与えられた重み付きグラフ G=(V,E) に対する最小全域木の辺の重みの総和を計算するプログラムを作成してください。
"""
import heapq
V, E = map(int,input().split())
G = [[] for v in range(V)]
for e in range(E):
    s, t, w = map(int,input().split())
    G[s].append((t,w))
    G[t].append((s,w))
    
visited = [0] * V # 訪問フラグ
pq = [] # 優先度付きキュー
for t, w in G[0]: # 始点はどこでも良いので、0とする
    heapq.heappush(pq, (w, t)) # (重み, ノードの終点)をキューに追加
visited[0] = 1

ans = 0
while pq:
    w, t = heapq.heappop(pq) # 重みが最小の辺を取り出す
    if visited[t] == 1: # 訪問済みならスキップ
        continue
    visited[t] = 1 # 訪問フラグを立てる
    ans += w # 重みを加算
    for s, w in G[t]: # t に隣接するノード s について
        heapq.heappush(pq, (w, s)) # 未探索なら探索候補としてキューに追加

print(ans)
