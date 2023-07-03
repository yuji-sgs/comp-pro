"""
長さ nの数列 Aと整数 mに対して、Aの要素の中のいくつかの要素を足しあわせて mが作れるかどうかを判定するプログラムを作成してください。
Aの各要素は1度だけ使うことができます。
数列 Aが与えられたうえで、質問として q個の miが与えれるので、それぞれについて "yes" または "no" と出力してください。
"""
n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

# Aの全ての部分和を求める
sums = set()
for i in range(1 << n):
    sum = 0
    for j in range(n):
        if (i >> j) & 1:
            sum += A[j]
    sums.add(sum)

# 各mについて、部分和の中に存在するか判定
for mi in m:
    if mi in sums:
        print('yes')
    else:
        print('no')
