"""
整数 n を素因数分解してください。
"""

# 素因数分解
def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n: # これ以上の i を試す必要がない
        if n % i: # 割り切れないなら
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1: # ループを抜けた後、もし n が1より大きいならば
        factors.append(n)
    return factors

n = int(input())
ans = prime_factorization(n)
ans = ' '.join(map(str, ans))
print("{}: {}".format(n, ans))
