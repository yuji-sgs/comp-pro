"""
深さ優先検索 (DFS) は、可能な限りグラフ内を「より深く」検索する戦略に従います。
DFS では、未探索のエッジが残っている最も最近発見された頂点 $v$ からエッジが再帰的に探索されます。
$v$ のエッジがすべて探索されると、探索は「バックトラック」して、$v$ が発見された頂点から離れてエッジを探索します。

このプロセスは、元のソース頂点から到達可能なすべての頂点が検出されるまで続きます。
未検出の頂点が残っている場合は、そのうちの 1 つが新しいソースとして選択され、そのソースから検索が繰り返されます。

DFS は、各頂点に次のようにタイムスタンプを付けます。
・ $d[v]$ は、$v$ が最初に発見されたときを記録します。
・ $f[v]$ は、検索が $v$ の隣接リストの検査を終了したときを記録します。

有向グラフ $G = (V, E)$ を読み取り、次の規則に基づいてグラフ上で DFS を実証するプログラムを作成します。
・ $G$ は隣接リストで指定されます。頂点はそれぞれ ID $1、2、... n$ によって識別されます。
・ 隣接リストの ID は昇順に並べられます。
・ プログラムは各頂点の検出時間と終了時間を報告する必要があります。
・ DFS 中に訪問する候補が複数ある場合、アルゴリズムは最小の ID を持つ頂点を選択する必要があります。
・ タイムスタンプは 1 から始まります。
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    V = list(map(int, input().split()))
    for v in V[2:]:
        G[i].append(v-1) # 0から始まるインデックスを考慮して-1する
        
D = [0] * N # 検出時刻
F = [0] * N # 終了時刻

def dfs(v, t): # v:頂点番号, t:時刻
    t += 1 # 発見したらインクリメント
    D[v] = t
    for next in G[v]:
        if D[next] == 0: # 未発見なら
            t = dfs(next, t)
    t += 1 # 完了してもインクリメント
    F[v] = t
    return t

t = 0
for n in range(N):
    if D[n]==0: # 未探索なら
        t = dfs(n,t)
    print (n+1,D[n],F[n])
