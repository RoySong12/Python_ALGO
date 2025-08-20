# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]


#     A = [[0] * N for _ in range(N)]
#     B = [[0] * N for _ in range(N)]
#     C = [[0] * N for _ in range(N)]

#     '''
#     90도 회전 (i,j) -> (j, N-1-i)
#     180도 회전 (i,j) -> (N-1-i, N-1-j)
#     270도 회전 (i, j) -> (N-1-j, i)'''



#     for i in range(N):
#         for j in range(N):
#             result = board[i][j]
#             A[j][N-1-i] = result
#             B[N-1-i, N-1-j] = result
#             C[N-1-j, i] = result

#     print(f"#{tc}")
#     for i in range(N):
#         s1 = ''.join(map(str, A[i]))
#         s2 = ''.join(map(str, B[i]))
#         s3 = ''.join(map(str, C[i]))
#         print(s1, s2, s3)




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{tc}")
    for i in range(N):
        A = ''.join(str(board[N-1-j][i]) for j in range(N))

        B = ''.join(str(board[N-1-i][N-1-j]) for j in range(N))

        C = ''.join(str(board[j][N-1-i]) for j in range(N))

        print(A, B, C)