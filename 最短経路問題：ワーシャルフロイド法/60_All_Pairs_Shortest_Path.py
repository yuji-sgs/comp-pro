"""
重み付き有向グラフ G=(V,E)の全点対間最短経路の距離を列挙してください。
"""
V, E = map(int, input().split())
INF = float('inf')

G = [[INF] * V for _ in range(V)]
for v in range(V):
    G[v][v] = 0
    
for e in range(E):
    s, t, d = map(int, input().split())
    G[s][t] = d
    
# ワーシャルフロイド法
for i in range(V): # 経由する頂点
    for j in range(V): # 始点
        for k in range(V): # 終点
            G[j][k] = min(G[j][k], G[j][i] + G[i][k])      
          
# 負の閉路が存在するかどうか
for v in range(V):
    if G[v][v] < 0:
        print('NEGATIVE CYCLE')
        exit()
        
# 結果出力
for g in G:
    g = [str(i) if i != INF else 'INF' for i in g]
    print(' '.join(g))
