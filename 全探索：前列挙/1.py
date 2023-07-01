"""
1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる組み合わせの数を求めるプログラムを作成して下さい。
n、x がともに 0 のとき入力の終わりとします。
"""

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0: # n、x がともに 0 のとき入力の終わり
        break
    
    count = 0

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            k = x - i - j
            if j < k <= n:
                count += 1
                    
    print(count)
