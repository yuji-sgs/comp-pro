"""
２つの整数 m, nについて、m^nを1,000,000,007で割った余りを求めてください。
"""

MOD = 10**9+7
m, n = map(int, input().split())
ans = pow(m,n,MOD) # pow(x,y,z)はx^yをzで割った余りを求める関数
print (ans)
