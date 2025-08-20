T = int(input())
A = list(range(1,13))

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        picked =0 
        total = 0
        for j in range(12):
            if i & (1<< j):
                picked += 1
                total += A[j]
        if picked == N and total == K:
            cnt += 1

    print(f"#{tc} {cnt}")

