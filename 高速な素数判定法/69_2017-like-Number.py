"""
「N も (N+1)÷2 も素数」を満たす奇数 N を 2017に似た数 とします。
Q 個のクエリが与えられます。
クエリ i(1≦i≦Q) では奇数li,riが与えられるので、li≦x≦riかつ 2017に似た数 となる奇数 x の個数を求めてください。
"""

N = 10 ** 6
dp = [1] * (N + 1)
dp[0] = dp[1] = 0

# エラトステネスの篩
for i in range(2, N+1):
    if dp[i] == 1: # iが素数の場合 
        for j in range(i*i, N+1, i): # iの倍数をふるい落とす
            dp[j] = 0

like2017 = [0] * (N + 1) # 2017に似た数の個数を格納する配列

# 2017に似た数の個数を求める
for n in range(N+1):
    if dp[n] == 0: # nが素数でない場合はスキップ
        continue 
    query = (n+1) // 2
    if dp[query] == 1:
        like2017[n] = 1
        
# 累積和を求める
for n in range(N):
    like2017[n+1] += like2017[n]

Q = int(input())
for q in range(Q):
    l, r = map(int,input().split())
    print (like2017[r]-like2017[l-1])
