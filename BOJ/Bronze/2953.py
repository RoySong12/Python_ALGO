
score = []
for _ in range(5):
    line = list(map(int, input().split()))
    line_sum = 0
    for s in line:
       line_sum += s
    score.append(line_sum)

ans = max(score)
idx = score.index(ans)+1

print(idx, ans)