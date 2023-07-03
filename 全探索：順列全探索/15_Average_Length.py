"""
座標平面上に N 個の町があります。町 i は、座標 (xi,yi) に位置しています。
町 i と町 j の間の距離は((xi - xj)^2 + (yi - yj)^2)^(1/2)です。
これらの町を全て 1 回ずつ訪れるとき、町を訪れる経路は全部で N! 通りあります。
1 番目に訪れる町から出発し、2 番目に訪れる町、3 番目に訪れる町、…、を経由し、N 番目に訪れる町に到着するまでの移動距離 (町から町への移動は直線移動とします) を、その経路の長さとします。
これらの N! 通りの経路の長さの平均値を計算してください。
"""
import numpy as np

N = int(input())
ans = 0

# 町の座標をタプル形式で格納
town = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        ans += np.sqrt((town[i][0] - town[j][0])**2 + (town[i][1] - town[j][1])**2)
        
        
print(ans / N)
