"""
自己ループと二重辺を含まない N 頂点 M 辺の無向連結グラフが与えられます。
i(1≦i≦M) 番目の辺は頂点aiと頂点biを結びます。
グラフから辺を取り除いたとき、グラフ全体が非連結になるような辺のことを橋と呼びます。
与えられた M 本のうち橋である辺の本数を求めてください。
"""
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


N, M = map(int, input().split())
uf = UnionFind(N)

edges = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 0-indexed
    b -= 1  # 0-indexed
    edges.append((a, b))

bridge = 0

for i in range(M): # 取り除く辺番号
    uf = UnionFind(N)  # 毎回新たなUnion-Find木を作る
    
    # i番目の辺だけを取り除いたグラフを作成
    for j in range(M):
        if i == j:
            continue  # i番目の辺は取り除く（結合しない）
        uf.unite(edges[j][0], edges[j][1])

    # 辺の両端が同じ連結成分に属しているかをチェック
    if not uf.issame(edges[i][0], edges[i][1]):
        bridge += 1

print(bridge)
