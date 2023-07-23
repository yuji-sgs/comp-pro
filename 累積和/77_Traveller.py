"""
あなたは JOI 街道を旅する旅人である. JOI 街道は東西にまっすぐに延びた道路で, JOI 街道上には n 個の宿場町がある．
宿場町には西から東の順に 1 から n までの番号が付けられている. 
JOI 街道上の最も西の宿場町が宿場町 1 であり，最も東の宿場町が宿場町 n である．
あなたは，宿場町 1 から出発して m 日間の旅に出ることになった．
あなたの旅程は数列 a1, a2, . . . , am に従い, 次のように決められている. 
ai は i 日目の移動方法を表す 0 ではない整数である. 
i 日目にあなたが出発する宿場町を宿場町 k とおくと，
i 日目にあなたは宿場町 k から宿場町 k +ai までまっすぐに移動することを意味する．
宿場町の個数 n,旅の日数 m, 宿場町間の距離の情報と，移動方法を表す数列
a1, a2, . . . , am が与えられたとき, m 日間の旅におけるあなたの移動距離の合計を
100000 = 10^5 で割った余りを求めるプログラムを作成せよ．
"""

import itertools
MOD = 10**5

# 入力
n, m = map(int, input().split())
town = [0] + [int(input()) for _ in range(n-1)]
a = [int(input()) for _ in range(m)]

ans = 0
town_csum = list(itertools.accumulate(town)) # 累積和

cur = 1 # 宿場町1からスタート
ans = 0

for c in a:
    next = cur + c # aの値だけ次の移動開始地点を進める
    ans += abs(town_csum[next-1] - town_csum[cur-1]) # 絶対値を足す
    cur = next # 次の移動開始地点
    ans %= MOD

print(ans)
