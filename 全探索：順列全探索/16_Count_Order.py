"""
大きさ N の順列 ((1, 2, ..., N) を並び替えてできる数列) P, Q があります。
大きさ N の順列は N! 通り考えられます。
このうち、P が辞書順で a 番目に小さく、Q が辞書順で b 番目に小さいとして、|a-b| を求めてください。
"""

from itertools import permutations

# 入力
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

# 1からNまでの数列を作成
numbers = list(range(1, N + 1))

# 順列を生成し、リストに格納
permutation = list(permutations(numbers))

# PとQの辞書順の位置を見つける
for i in range(len(permutation)):
    if permutation[i] == P:
        a = i
    if permutation[i] == Q:
        b = i

# |a-b|を計算して出力
print(abs(a - b))
