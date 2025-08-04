T= int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    min_num = 999999999
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        result = max_num - min_num
    print(f"#{i} {result}")