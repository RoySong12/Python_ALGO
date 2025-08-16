T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N):
        for j in range(N):

            s_plus = board[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1, M):
                    ni, nj = i + di*c, j + dj * c
                    if 0<= ni < N and 0 <= nj < N:
                        s_plus += board[ni][nj]


            s_diag = board[i][j]
            for di, dj in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for c in range(1, M):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0<= nj < N:
                        s_diag += board[ni][nj]

            if s_plus > max_kill:
                max_kill = s_plus
            if s_diag > max_kill:
                max_kill = s_diag

    print(f"#{tc} {max_kill}")