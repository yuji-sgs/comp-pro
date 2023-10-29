"""
https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
"""
N, M = map(int, input().split())
score = [[] * N for _ in range(N)]
for i in range(N):
    A = list(map(int, input().split()))
    score[i] = A
max_score = 0

for t1 in range(M):
    for t2 in range(t1+1, M):
        current_score = 0
        for j in range(N):
            if t1 == t2:
                continue
            current_score += max(score[j][t1], score[j][t2])
        max_score = max(max_score, current_score)
        
print(max_score)        
