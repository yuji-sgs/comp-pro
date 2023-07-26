"""
皆さんはあるパズルに取り組んでいる． このパズルには,下図に示すような, H 行, 5 列のセルからなる，直立した盤を使う． 
各セルには1から9までの数字が1つ刻まれた石が配置されている.  3個以上の水平に隣り合うセルに同じ数字を彫った石があれば, これらの石は消滅する．
石が消滅したセルの上方のセルに石があれば，それらは順次落ちて空きを埋める．

パズルは以下のステップに従って進行する．
1. 3個以上の水平に隣り合うセルに同じ数字を彫った石があれば, これらの石は消滅する．こうした石群の消滅はすべて同時に起きる．
2. 石が消滅したセルの上方のセルに石があれば，空きを埋めるように石が落下する．
3. すべての石の落下完了後に, 消滅の条件を満たすようになった石群があれば, ステップ1に戻って繰り返す. 

このパズルのスコアは消滅した石の数字の合計である．
与えられた石の配置で獲得できるスコアを計算するプログラムを作れ．
"""

# 石の落下
def move(board):
    board = [list(x) for x in zip(*board)] # 転置（列方向の操作を簡単にするため）
    for i in range(len(board)): # 各行について
        row = board[i] # i番目の行を取り出す
        row = [i for i in row if i != 0] # 0以外の(石が存在する)要素を取り出す
        n = len(board[i]) - len(row) # 0の(石が消滅した)個数を数える
        row.extend([0] * n) # 石を落下
        board[i] = row # 落下後の行を代入
    board = [list(x) for x in zip(*board)] # 転置して、元に戻す
    return board

ls_ans = []
while(1): # 無限ループ
    ans = 0
    H = int(input())
    
    if H == 0: # 0が入力されたら終了
        break
    
    board = []
    for h in range(H):
        board.append(list(map(int, input().split())))
    board = board[::-1] # 逆順にする
    
    for t in range(H): 
        for h in range(H): 
            C = board[h] # h番目の行を取り出す
            changed = set()
            old_c = "" # 1つ前の石の数字
            oldold_c = "" # 2つ前の石の数字
            streak = 0 # 連続した石の数字の合計
            for i,c in enumerate(C): # 各石について
                if c == old_c and c == oldold_c: 
                    if streak == 0: # 3つ連続した石が初めて現れた場合
                        streak += 3 * c  # 3つ連続した石の数字の合計を計算
                        C[i] = C[i-1] = C[i-2] = 0  # 3つ連続した石を消滅させる
                    else:  # 4つ以上連続した石が現れた場合
                        streak += c # 3つ連続した石の数字の合計に加算
                        C[i] = 0 # 4つ目以降の石を消滅させる
                else: # 連続した石が途切れた場合
                    ans += streak # 連続した石の数字の合計をスコアに加算
                    streak = 0 # 連続した石の数字の合計をリセット
                oldold_c = old_c # 2つ前の石の数字を更新
                old_c = c # 1つ前の石の数字を更新
            ans += streak # 行の最後の石について、連続した石の数字の合計をスコアに加算
            board[h] = C # 更新した行を元の盤に代入
        board = move(board) # 石を落下させる
    ls_ans.append(ans) # 最終的なスコアをリストに追加

for ans in ls_ans:
    print(ans)
