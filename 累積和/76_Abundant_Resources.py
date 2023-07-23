"""
東西に細長い土地があります。 
この土地は、N 個の区画が東西に並んだ形をしており、西から i 番目の区画は区画 i と呼ばれます。
それぞれの区画には地下資源があることがわかっており、区画 i の資源埋蔵量はAiです。
1 以上 N 以下のそれぞれの整数 k について、次の問題の答えを求めてください。
・連続する k 個の区画を選んだとき、それらの区画の資源埋蔵量の総和として考えられる最大値はいくらか。
"""

from itertools import accumulate
N = int(input())
A = [0] + list(map(int, input().split())) # A[0]は0にしておくことで、インデックスと区画番号が一致するようにする。
acc = list(accumulate(A)) # 累積和

for i in range(1, N+1): # 区画の数
    ans = 0 # k区画の資源埋蔵量の総和の最大値の初期化
    for j in range(N-i+1): # 区画の始点
        diff = acc[j+i] - acc[j] # 区画jから区画j+iまでの資源埋蔵量の総和
        ans = max(ans, diff)
    print (ans)
    
print(acc)
