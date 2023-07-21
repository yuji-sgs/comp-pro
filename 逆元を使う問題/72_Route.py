"""
横 W x 縦 H のグリッドがあります。
左から i 番目、下から j 番目のマス目には (i,j) という番号がついています。
高橋君は、マス目 (i,j) から (i+1,j) または (i,j+1) に進むことができます。
高橋君が (1,1) から (W,H) まで行く経路の個数を 1,000,000,007 で割ったあまりを求めてください。
"""
import math
def com_cnt(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

MOD = 10**9+7
W,H = map(int,input().split())
W -= 1
H -= 1

print(com_cnt(W + H, W) % MOD)
