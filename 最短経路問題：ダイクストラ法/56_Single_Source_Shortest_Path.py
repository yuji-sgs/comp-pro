"""
与えられたグラフ G=(V,E)と始点 rについて、単一始点最短経路の重みを求めるプログラムを作成してください。
Gのノードrを始点とし、rから各ノードについて、最短経路上の辺の重みの総和を出力してください。
"""

# 入力の受け取り
V, E, r = map(int, input().split())
G = [[] for i in range(V)] # G[i]: ノードiに隣接するノードのリスト

for e in range(E):
    s, t, d = map(int, input().split()) # s:始点, t:終点, d:重み
    G[s].append((t, d)) # G[始点] = (終点, 重み)
    
INF = 99999 
dist = [INF] * V # 各ノードまでの距離を格納するリスト
flg = [0] * V # 各ノードの最短距離が確定したかどうかを格納するリスト
dist[r] = 0 # 始点の距離は0

for i in range(V):
    d = INF # 最短距離を格納する変数
    for j in range(V):
        if flg[j] == 0 and dist[j] < d: # 最短距離が未確定のノードの中で、最も距離が小さいノードを見つかった時
            p = j # 最短距離が小さいノードの番号をpに格納
            d = dist[j] # 最短距離をdに格納
    flg[p] = 1 # 最短距離が確定したノードを1にする
    for j, c in G[p]:  # ノードpから到達できる全てのノードについて
        if dist[j] > dist[p] + c: # 頂点p経由でjに行く方が近ければ、
            dist[j] = dist[p] + c  # dist[j]を更新

# 結果を出力
for i in range(V):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])


"""
計算量を落とすには、優先度つきキューを使う。

import heapq
INF = 10**10

V, E, r = map(int,input().split())
adj = [[] for i in range(V)] # 隣接リスト

for e in range(E):
    s, t, d = map(int,input().split())
    adj[s].append((t,d))

dists  = [INF for i in range(V)] # 重みの和
dists[r] = 0
pq = [(0, r)] # 二分ヒープの実体はリストやタプルとして表現する  (重みの和, ノード番号)
while(pq):
    d, node = heapq.heappop(pq)
    if (d > dists[node]): # 探索の対象にする必要があるか確認
        continue
    for next, cost in adj[node]:
        if d + cost < dists[next]:# 探索の対象にする必要があるか確認
            dists[next] = d + cost # 次のノードにおける重みの和
            heapq.heappush(pq, (dists[next],next))
for d in dists:
    if d == INF:
        print ('INF')
    else:
        print (d)    
"""
