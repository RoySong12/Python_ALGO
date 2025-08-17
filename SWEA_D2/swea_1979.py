T = int(input())
 
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    result = 0
 
    # 가로줄
    for i in range(N):
        count = 0  #연속된 흰색 부분 길이 세기
        for j in range(N):
            if board[i][j] == 1:   
                count += 1   
            else:
                if count == K: #검은색 부분 나오기 전까지 K완성한 경우
                    result += 1
                count = 0
        if count == K:   #행의 끝 부분에서도 마지막으로 세주기
            result += 1
 
    # 세로줄
    for j in range(N):
        count = 0
        for i in range(N):
            if board[i][j] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        if count == K:  
            result += 1
 
    print(f"#{tc} {result}")