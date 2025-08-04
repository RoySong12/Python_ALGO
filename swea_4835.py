T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr =list(map(int, input().split()))



    min_v = 9999999999999999999999
    max_v = 0
    #for j in arr:보다는 index를 가지고 생각해야함
    for j in range(0, N-M+1):
        s = sum(arr[j:j+M])

        if s > max_v:
            max_v =s
        if s < min_v:
            min_v =s
    print(f"#{i} {max_v -min_v}")

    

