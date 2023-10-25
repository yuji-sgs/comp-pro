"""
英大文字からなる文字列 S が与えられます。
S の部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。
ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。
"""
S = input()
target_str = ['A', 'C', 'G', 'T']
ans = 0
current = 0

for s in S:
    if s in target_str:
        current += 1
        ans = max(ans, current)
    else:
        current = 0
        
print(ans)
