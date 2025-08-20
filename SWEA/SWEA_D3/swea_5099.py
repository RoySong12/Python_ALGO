T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    oven = []  # 피자번호, 치즈
    

    next_idx = 0  # 다음 넣을 피자 
    for _ in range(N):
        oven.append((next_idx + 1, cheeses[next_idx]))
        next_idx += 1

    
    while len(oven) > 1:
        idx, cheese = oven.pop(0)   # 맨 앞의 피자 꺼내기
        cheese //= 2                
        if cheese == 0:             # 다 녹았을 때
            if next_idx < M:    
                oven.append((next_idx + 1, cheeses[next_idx]))
                next_idx += 1
        else:
            oven.append((idx, cheese)) 

    print(f"#{tc} {oven[0][0]}")


