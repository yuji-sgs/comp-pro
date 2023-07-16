"""
n個の行列の連鎖 M1,M2,M3,...,Mnが与えられたとき、スカラー乗算の回数が最小になるように積 M1M2M3...Mnの計算順序を決定する問題を連鎖行列積問題(Matrix-Chain Multiplication problem)と言います。
n個の行列について、行列 Miの次元が与えられたとき、積 M1M2...Mnの計算に必要なスカラー乗算の最小の回数を求めるプログラムを作成してください。

◎入力
入力の最初の行に、行列の数 nが与えられます。
続く n行で行列 Mi(i=1...n)の次元が空白区切りの２つの整数 r、cで与えられます。
rは行列の行の数、cは行列の列の数を表します。
"""

INF = 10**10
N = int(input())
dp = [[INF] * N for _ in range(N)]
R = []
for n in range(N):
    r, c = map(int,input().split())
    R.append(r)
R.append(c) # 最後の行列の列数を追加することで、1次元配列で連鎖行列積を表現

for i in range(N):
    dp[i][i] = 0 # 対角成分すなわち、行列積Miを計算するコストは0である（単一の行列を乗算するというのは、実質的に何も操作を行わないことを意味するため）

for l in range(1,N): # 連鎖行列積の範囲（lはiとjの差分）
    for i in range(N-l): # 連鎖行列積の開始位置を表すi
        j = i+l  # 連鎖行列積の終了位置を表すj
        for k in range(i,j): # 連鎖行列積の分割位置を表すk
            # cost(左側行列積) + cost(右側行列積) + 行列計算のコスト
            tmp = dp[i][k] + dp[k+1][j] + R[i] * R[k+1] * R[j+1] # R[i] * R[k+1] * R[j+1]は、行列積の計算に必要なスカラー乗算の回数を表す。
            dp[i][j] = min(dp[i][j], tmp)
            
print (dp[0][-1])
