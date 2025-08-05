T = int(input())

def count_charge(K,N,M,chargers):
    idx = 0 
    count = 0 

    while idx < N: #True는 반복, False는 종료
        num = [c for c in chargers if idx < c and c <= idx + K]

        if idx + K >= N:
            return count # 더이상 충전 필요 없어
        if len(num) == 0 : 
            return 0
        else:
            idx = max(num)
            count += 1


for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))

    chargers = list(map(int, input().split()))


    #종점까지 가는 최소 충전 횟수
    count = count_charge(K,N,M, chargers)
    print(f"#{tc} {count}")