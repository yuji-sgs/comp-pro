"""
与えられた有向グラフ G=(V,E)について、頂点 1から各頂点への最短距離 d（パス上の辺の数の最小値）を求めるプログラムを作成してください。
各頂点には 1から nまでの番号がふられているものとします。頂点 1からたどり着けない頂点については、距離として-1 を出力してください。
"""
from collections import deque

N = int(input())
g = [[] for _ in range(N)]

for i in range(N):
    # 隣接している頂点のみ取得
    _, _, *v = map(lambda x: int(x)-1, input().split())
    g[i] = v
    
# 幅優先探索用のキュー
q = deque()
q.append(0)

# 各頂点への最短距離を格納するリスト
dist = [-1] * N
dist[0] = 0

# 幅優先探索
while len(q) > 0:
    v = q.popleft()
    
    # 隣接している頂点を探索
    for nv in g[v]:
        
        # すでに探索済みの場合はスキップ
        if dist[nv] != -1:
            continue
        
        # 距離を更新してキューに追加
        dist[nv] = dist[v] + 1
        q.append(nv)

for i in range(N):
    print(i+1, dist[i])
