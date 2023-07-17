"""
E869120は, セールスマンである。だから, すべての建物を
1度ずつ通って店に戻ってこなければならない。

E869120の住む街には, 建物がN個あり, 道路がM本ある。建物の番号は1-indexedでつけられており, 店は建物1とする。
また, 道路 i は建物siと建物tiを結んでいて, 距離はdiである。
しかし, その街は不審者対策として一定の時間を過ぎると道路を閉鎖する。
道路iは, E869120が出発してから時間 time_i経つと道路が閉鎖される。
だから, その道路を通る際, 時間 time_i以内に道路を通り終えなければならない。
そのとき, E869120は次のようなことを考えた。
「最短時間で戻ってくる方法の総数はどのくらいあるのだろう？」
そこで, 優秀なプログラマーであるあなたにプログラムを作ってもらうことになりました。
最短経路と, 最短時間で戻ってくる方法の総数を求めなさい。
ただし, E869120は時間 1 につき距離 1 進む。また, 道路は双方向に移動可能である。
"""
from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, input().split())

INF =  float('inf')
cost = [[[INF, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, t, d, time = map(int, input().split())
    cost[s-1][t-1] = [d, time]
    cost[t-1][s-1] = [d, time]
 
dp = [[[-1] * 2 for _ in range(N)] for _ in range(1<<N)]
dp[0][0]=[0, 1]
 
def dfs(S, v):
    if dp[S][v] != [-1, -1]:
        return dp[S][v]
 
    if S&(1<<v) == 0:
        dp[S][v] = [INF, 0]
        return dp[S][v]
    
    v_time = INF
    v_s = 0
    for prev in range(N):
        prev_time, prev_s = dfs(S^(1<<v), prev)
        if prev_time + cost[prev][v][0] > cost[prev][v][1]:continue
        if v_time > prev_time + cost[prev][v][0]:
            v_time = prev_time + cost[prev][v][0]
            v_s = prev_s
        elif v_time == prev_time + cost[prev][v][0]:
            v_s += prev_s
    
    dp[S][v] = [v_time, v_s]
    return dp[S][v]
 
ans1, ans2 = dfs((1<<N)-1, 0)
if ans1 == INF:
    print("IMPOSSIBLE")
else:
    print(ans1, ans2)
