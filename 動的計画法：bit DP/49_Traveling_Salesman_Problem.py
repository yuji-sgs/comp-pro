"""
重み付き有向グラフ G(V,E) について、以下の条件を満たす最短経路の距離を求めて下さい：
・ある頂点から出発し、出発点へ戻る閉路である。
・ 各頂点をちょうど１度通る。
"""

V, E = map(int, input().split())
INF = 10**10
cost = [[INF] * V for _ in range(V)] # 重みをINFで初期化
for e in range(E):
    s, t, d = map(int,input().split())
    cost[s][t] = d # 重みを代入

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]:訪問状況がSで、現在地が頂点vであるときの最小コスト

def dfs(S, v, dp):
    if dp[S][v] != -1: # 訪問済みならメモを返す
        return dp[S][v]
    if S==(1<<V)-1 and v==0: # 全ての頂点を訪れて頂点0に戻ってきた
        return 0 # もう動く必要はない

    res = INF
    for u in range(V):
        if S>>u & 1 == 0: # 未訪問かどうか(ビット集合Sをuビット右にシフトして、最下位ビットが0かどうか)
            res = min(res, dfs(S|1<<u, u, dp)+cost[v][u]) # S|1<<uでビット集合Sに頂点uを追加し（つまり、頂点uを訪問済みにし）、頂点uから頂点vに移動するコストを加算する
    dp[S][v] = res
    return res

ans = dfs(0, 0, dp) # 頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print (ans)
