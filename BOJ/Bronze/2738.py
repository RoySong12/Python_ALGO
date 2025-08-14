N, M = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(N)]

B = [list(map(int, input().split())) for _ in range(N)]

result = []

for i in range(N):
    line = []
    for j in range(M):
        line.append(A[i][j] + B[i][j])
    result.append(line)

for r in result:
    print(*r)
