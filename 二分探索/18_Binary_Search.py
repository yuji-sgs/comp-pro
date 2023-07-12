"""
n個の整数を含む数列 Sと、q個の異なる整数を含む数列 Tを読み込み、
Tに含まれる整数の中で Sに含まれるものの個数 Cを出力するプログラムを作成してください。
"""
def binary_search(S, key):
    left = 0
    right = len(S)
    while left < right:
        mid = (left + right) // 2
        if S[mid] == key:
            return True
        elif key < S[mid]:
            right = mid
        else:
            left = mid + 1
    return False
            

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = 0
S.sort()

for i in range(q):
    if binary_search(S, T[i]):
        C += 1
    
print(C)
