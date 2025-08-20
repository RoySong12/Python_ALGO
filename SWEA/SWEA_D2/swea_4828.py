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





'''8/14
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))

    min_num = 100000000000000
    max_num = 0

    for i in range(N):   #굳이 range()로 뽑지말고 리스트에서 하나씩 뽑아오자
        if line[i] < min_num:
            min_num = line[i]
        if line[i] > max_num:
            max_num = line[i]
        result = max_num - min_num
    
    print(f"#{tc} {result}")
'''


