"""
JOI 国には、n 島の島があり，各島には 1 から n までの番号が付けられている。現在、JOI 国では各島の間を結ぶ航路網の整備が進んでいる．
あなたは、船舶の切符を扱っているチケットセンターに勤務している。JOI 国には船舶を使って，できる限り安価に，島と島の間を旅行したいと考えている人が沢山おり，彼らは，出発地と目的地を注文票に記入して，あなたのところに送ってくる．
あなたの仕事は，客から注文票を受け取ったらすぐに，いくつかの船舶を乗り継いで，出発地と目的地を結ぶ航路の中で，もっとも安価な運賃を計算し，客に伝えることである．
ただし、旅程によっては、船舶を使って旅行することが出来ない場合もある。そのときは『船舶を使って旅行することが出来ない』と客に伝える必要がある。
また、JOI 国では，島と島の間を結ぶ新しい船舶が，次々と運航を開始しており，あなたには，その情報が随時伝えられる．客に返事をする際には，最新の情報に留意しなければならない．
入力として，客の注文票や新たに運航を開始した船舶の運航情報が与えられたときに，客への返事を求めるプログラムを作成せよ．
なお，入力例 1 と出力例 1 に対する実行状況を，図 1 として図示している．
"""
import heapq
INF = 10**10

def dijkstra(s, g): # s: スタート, g: ゴール
    dists  = [INF for i in range(N)] # 各ノードまでの距離を格納するリスト
    dists[s] = 0 # 始点の距離は0
    pq = [(0, s)] # 優先度付きキューのオブジェクトそのものはただのリスト | (重みの和, ノード番号)
    while(pq): # キューが空になるまで
        d, node = heapq.heappop(pq) # キューから重みの和が最小の要素を取り出す
        if (d > dists[node]): # 探索の対象にする必要があるか確認
            continue
        for next, cost in adj[node]: # node に隣接しているノード next について
            if d + cost < dists[next]: # 更新すべきか確認
                dists[next] = d + cost # 更新
                heapq.heappush(pq, (dists[next],next)) # キューに追加
    if dists[g] == INF:
        return -1
    else:
        return dists[g]

N, K = map(int,input().split())
adj = [[] for i in range(N)] # 隣接リスト
ans = []
for k in range(K):
    ls = list(map(int,input().split()))
    if ls[0]==0:
        ans.append(dijkstra(ls[1]-1, ls[2]-1)) # Pythonでは0から始まるので-1
    else:
        adj[ls[1]-1].append((ls[2]-1,ls[3])) #重みは-1しないことに注意
        adj[ls[2]-1].append((ls[1]-1,ls[3]))

for a in ans:
    print (a)
