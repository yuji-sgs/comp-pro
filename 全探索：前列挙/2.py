"""
105 という数は, 非常に特殊な性質を持つ - 奇数なのに, 約数が 8 個もある.
さて, 1 以上 N 以下の奇数のうち, 正の約数を ちょうど 8 個持つようなものの個数を求めよ.
"""

def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

N = int(input())
ans = 0

for j in range(1, N+1):
    if j % 2 == 1 and divisor(j) == 8:
        ans += 1
        
print(ans)