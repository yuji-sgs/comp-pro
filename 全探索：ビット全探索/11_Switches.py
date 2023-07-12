"""
on と off の状態を持つ N 個の スイッチと、M 個の電球があります。
スイッチには 1 から N の、電球には 1 から M の番号がついています。
電球 i はki個のスイッチに繋がっており、スイッチ si1,s i2,...,siki のうち on になっているスイッチの個数を 2 で割った余りがpiに等しい時に点灯します。
全ての電球が点灯するようなスイッチの on/off の状態の組み合わせは何通りあるでしょうか。
"""

# 入力
N, M = map(int, input().split())
bulbs = []
for _ in range(M):
    b = tuple(map(int, input().split()))
    bulbs.append(b[1:]) # b[0]は要らないので、b[1:]でスライス
P = list(map(int, input().split())) # 電球のon/offの状態

# ansの初期化
ans = 0

# bit全探索
for switch in range(1 << N): # N個のスイッチの全てのon/off状態の組み合わせを探索
    check = [False] * M # M個の電球のon/offの状態を格納するリスト
    
    # 電球のon/offの状態をチェック
    for i, bulb in enumerate(bulbs): # bulbsリストの中をenumerateでループ
        cnt = 0 # 電球に繋がっているスイッチのonの数
        for b in bulb: # 電球に繋がっているスイッチの中をループ
            if switch >> (b - 1) & 1: # switchのb-1番目のbitが1ならば
                cnt += 1 # cntを1増やす

        if cnt % 2 == P[i]:
            check[i] = True
        else:
            check[i] = False

    if all(check):
        ans += 1

print(ans)
