"""
価値が vi 重さが wi であるような N 個の品物と、容量が W のナップザックがあります。
次の条件を満たすように、品物を選んでナップザックに入れます：
・ 選んだ品物の価値の合計をできるだけ高くする。
・ 選んだ品物の重さの総和は W を超えない。
価値の合計の最大値を求めてください。
"""

N, W = map(int, input().split())
v = []
w = []

for i in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)


# (N+1) x (M+1) の配列を用意する
# 配列全体を -1 で初期化する
dp = [[-1] * (W+1) for _ in range(N+1)]

# 初期状態
# 0 個の品物は、重さ 0 で価値は 0
dp[0][0] = 0

# 各品物を順に考慮していく (マス目を下へと更新していく)
for i in range(N):
    for j in range(W+1):
        # 最初の i 個の品物のみを用いて重さを j にすることが不可能の場合はスキップ
        if dp[i][j] < 0:
            continue

        # i 番目の品物を追加しない場合 (1 つ下のマスへ進む場合)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        # i 番目の品物を追加する場合 (1 つ下、A[i] つ右のマスへ進む場合)
        if j+w[i] <= W:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j] + v[i])

# 答え
print(max(dp[N]))
