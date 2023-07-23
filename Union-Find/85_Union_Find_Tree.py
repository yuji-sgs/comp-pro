"""
互いに素な動的集合 S=S1,S2,...,Sk を管理するプログラムを作成してください。
まず、整数 n を読み込み、0, 1, ... n-1 をそれぞれ唯一の要素とする n 個の互いに素な集合を作成します。
次に、整数q を読み込み、q 個のクエリに応じて集合を操作します。クエリは以下の2種類を含みます:
・unite(x,y): x を含む集合 Sx と y を含む集合 Sy を合併する。
・same(x,y): x と y が同じ集合に属しているかを判定する。
"""
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n 
        
    def find(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.find(self.par[x]) # 経路圧縮
            return self.par[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: 
            return
        self.par[x] = y

n, q = map(int, input().split())
uf = UnionFind(n)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        uf.unite(x, y)
    elif com == 1:
        if uf.find(x) == uf.find(y):
            print(1)
        else:
            print(0)
