"""
フィボナッチ数列の第 n項の値を出力するプログラムを作成してください。
"""
# フィボナッチ数列を再帰関数で求める
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return(fib(n-1) + fib(n-2))
    
n = int(input())
print(fib(n))
