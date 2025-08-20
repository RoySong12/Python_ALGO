T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
 
    # 오 아래 왼 위
    di = [0, 1, 0, -1] #행
    dj = [1, 0, -1, 0] #열
 
    d = 0
    i, j = 0,0
    for num in range(1, N * N + 1):
        snail[i][j] = num
        ni, nj = i + di[d], j + dj[d] 
         
        if ni < 0 or ni >= N or nj <0 or nj >= N or snail[ni][nj] != 0:
            d = (d + 1) % 4 # 0,1,2, 3 순환해야해서 
            ni, nj = i + di[d], j + dj[d]
 
        i, j = ni, nj
 
     
    print(f"#{tc}")
    for row in snail:
        print(*row)