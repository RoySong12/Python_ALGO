T = int(input())

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    valid =1 



    #가로줄 검사
    for i in range(9):
        count =[0] * 10
        for j in range(9):
            num = board[i][j]
            count[num] += 1
        for k in range(1, 10):
            if count[k] != 1:
                valid = 0
                break
        # if not valid:  이미 가로줄 검사에서 valid가 아니면 밑에 할 필요가 없어서
        #     break
        

    #세로줄 검사    
    if valid:
        for j in range(9):
            count = [0] * 10
            for i in range(9):
                num = board[i][j]
                count[num] += 1
            for k in range(1, 10):
                if count[k] != 1:
                    valid = 0 
                    break
            #if not valid:  이미 가로줄 검사에서 valid가 아니면 밑에 할 필요가 없어서
                #break
    
    # 3*3 배열 검사
    if valid:
        for ni in range(0,9,3):
            for nj in range(0,9,3):
                count = [0] * 10
                for i in range(ni, ni+3):
                    for j in range(nj, nj+3):
                        num = board[i][j]
                        count[num] += 1
                for k in range(1, 10):
                    if count[k] != 1:
                        valid = 0
                        break
    print(f"#{tc} {valid}")