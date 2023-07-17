"""
数列 A=a0,a1,…,an-1 の最長増加部分列 (LIS: Longest Increasing Subsequence) の長さを求めてください。 
数列 A の増加部分列は 0≤i0<i1<…<ik<n かつ ai0<ai1<…<aik を満たす部分列 ai0,ai1,…,aik です。
最長増加部分列はその中で最も kが大きいものです。
"""
import bisect
n = int(input())
INF = 10 ** 10
dp = [INF] * n # dp[i]: 長さがi+1であるような増加部分列における最終要素の最小値

for i in range(n):
    a = int(input())
    idx = bisect.bisect_left(dp, a) # aを挿入できる位置を二分探索して左端のインデックスを取得
    dp[idx] = a # aを挿入
    
# 最後にINF以外の要素数を数える
print(bisect.bisect_left(dp, INF))
