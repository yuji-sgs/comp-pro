"""
二次元グリッドの原点 (0,0) にチェスのナイトの駒があります。
ナイトの駒はマス (i,j) にあるとき (i+1,j+2) か (i+2,j+1) のどちらかのマスにのみ動かすことができます。
ナイトの駒をマス (X,Y) まで移動させる方法は何通りありますか？
10^9+7 で割った余りを求めてください。
"""
MOD = 10**9+7
X, Y = map(int, input().split())

if (X > Y): # X > Y にすることで、考えやすくする
    X, Y = Y, X
if (X+Y)%3 != 0: # X+Y は 3 の倍数である必要がある
    print (0)
    exit()
if (2*X < Y): # Y方向にXの2倍以上動かすことはできない
    print (0)
    exit()
    
W = X - ((X+Y)//3)
H = Y - ((X+Y)//3)

mx = 10**6
fact = [1] * (mx+1) # 階乗を格納するリスト

def inv(n): # MODを法とした逆元
    return pow(n, MOD-2, MOD)

for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算
    
ans = (fact[W+H] * inv(fact[W]) * inv(fact[H])) % MOD # comb(W+H,W) = (W+H)!/(W!H!)
print (ans)
