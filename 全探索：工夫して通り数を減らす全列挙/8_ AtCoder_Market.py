"""
AtCoder マーケットは、1 000 000 000 個のマスが 1 列につながったマス目で表されるスーパーマーケットである。
ここでは、左から i 番目のマスを「マス i」とする。
ある日、N 人の買い物客が AtCoder マーケットに来る。i 人目の買い物客は、マス Aiにある品物とマス Biにある品物を買う。
square1001 君は、AtCoder マーケットに入口と出口を 1 つずつ設置することにした。入口と出口はいずれかのマス目に設置する。入口と出口は同じ場所にあってもよい。
そのとき、買い物客は次のような経路で移動する。
まず、入口からスタートする。マスAiと Biを経由して、出口でゴールする。
すべての買い物客について、隣り合ったマス目に進むのに 
1 秒かかるとき、最適に入口と出口を設置したときの「すべての買い物客の移動時間の合計」の最小値を求めなさい。
"""
import numpy as np

N = int(input())
A_list = []
B_list = []
ans = 0

# 絶対誤差の合計が一番小さいところに入口と出口を設置する
for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
    
# 絶対誤差の合計が一番小さいのは中央値
enter = int(np.median(A_list)) 
exit = int(np.median(B_list))
    
for i in range(N):
    ans += (abs(enter - A_list[i]) + abs(B_list[i] - A_list[i]) + abs(exit - B_list[i]))
    
print(ans)
