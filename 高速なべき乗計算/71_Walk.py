"""
E869120王国では, N個の街があり, 街i-1と街iは道路で結ばれている。
また, 街i(1≦i≦N)には整数aiが書かれており, 道路の長さは次の規則に従って定められる。
街i-1と街iを結ぶ道路の長さはai-1aiである。E869120王国に住むsquare1001は, 散歩をすることにした。
square1001は街1に住んでいて, 1->c1->c2->...->cQ->1というように散歩することになっている。
しかし, square1001はとんでもない距離を歩くかもしれないので, あなたはsquare1001のために歩く距離を教えてほしい。
square1001の歩く距離をmod 1,000,000,007で求めなさい。
"""

from itertools import accumulate
MOD = 10**9+7
N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [0]
for n in range(N-1):
    d = pow(A[n],A[n+1],MOD)
    D.append(d)
acc = list(accumulate(D)) # 累積和

C.insert(0,1) # 始点
C.append(1) # 終点
ans = 0
for q in range(len(C)-1):
    ans += abs(acc[C[q+1]-1]-acc[C[q]-1]) % MOD
print (ans%MOD) # 最後のMODを忘れずに
