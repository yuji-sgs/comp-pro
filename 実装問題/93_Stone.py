"""
square1001氏は、パソコン部に入るために試験を受けました。
この試験の内容は、以下のようなものであります。
・H*Wの盤面が与えられる。
・その盤面の各マスは、 1~9の数字が書かれている。また、1行目が一番上である。
・あなたは、セルのうち1つのマスを消すことができる。消した上のマスは落ちてくる。

また、そのゲームは以下のようなステップで進行する。
・1:K個以上の水平に隣り合うセルに同じ数字を彫った石があれば,これらの石は消滅する．こうした石群の消滅はすべて同時に起きる。
・2:石が消滅したセルの上方のセルに石があれば，空きを埋めるように石が落下する。
・3:すべての石の落下完了後に，消滅の条件を満たすようになった石群があれば,ステップ1に戻って繰り返す。
・4:スコアは, 2*i(i回目の消滅で消えた数字の値の和)の合計である。ただし、最初の消滅を0回目とする。
そのとき、square1001氏が最適にやって試験に受かるか調べるために、最適にセルを消したときに何点取れるかを計算することにした。
square1001氏を助けるために、最大の点数を出力しなさい。
"""
import sys
input = sys.stdin.readline
H, W, K = map(int, input().split())
B = [list(map(int, input()[:-1])) for _ in range(H)]

def calc(S):
    gain = 0
    for line in S:
        gain += clear(line)
    remove(S)
    return gain
 
 
def clear(line):
    gain = 0
    cnt = 0
    pre = line[0]
    for i, c in enumerate(line):
        if pre == c:
            cnt += 1
        else:
            if cnt >= K:
                gain += line[i-1]*cnt
                for k in range(i-cnt, i):
                    line[k] = 0
            cnt = 1
        pre = c
 
    if cnt >= K:
        gain += line[-1]*cnt
        for k in range(W-cnt, W):
            line[k] = 0
    return gain
 
 
def remove(S):
    for w in range(W):
        i = H-1
        for h in range(H-1, -1, -1):
            if S[h][w]:
                S[i][w] = S[h][w]
                i -= 1
        for i in range(i+1):
            S[i][w] = 0
 
 
def remove_sq(S, i, j):
    for h in range(i, 0, -1):
        S[h][j] = S[h-1][j]
    S[0][j] = 0
 
 
ans = 0
for i in range(H):
    for j in range(W):
        S = [b.copy() for b in B]
        remove_sq(S, i, j)
        score = 0
        p = 1
        while True:
            gain = calc(S)
            if gain == 0:
                break
            score += p * gain
            p *= 2
        if ans < score:
            ans = score
print(ans)
