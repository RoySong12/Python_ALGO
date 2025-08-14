# T = int(input())

# for i in range(1, T+1):
#     N, M = map(int, input().split())
#     arr =list(map(int, input().split()))



#     min_v = 9999999999999999999999
#     max_v = 0
#     #for j in arr:보다는 index를 가지고 생각해야함
#     for j in range(0, N-M+1):
#         s = sum(arr[j:j+M])

#         if s > max_v:
#             max_v =s
#         if s < min_v:
#             min_v =s
#     print(f"#{i} {max_v -min_v}")

    



T= int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_value = 0
    min_value = 99999999999

    for j in range(0, N-M+1):
        value = sum(arr[j:j+M])

        if value > max_value:
            max_value = value

        if value < min_value:
            min_value = value

        result = max_value - min_value
    print(f"#{i} {result}")




'''8/14
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    line = list(map(int, input().split()))

    max_sum = 0
    min_sum = 1000000000000

    for i in range(N-M+1):   #range()끝부분은 포함 안되는 거 꼭 신경 쓰기!!!
        count = line[i:i+M]
        result = sum(count)
        if max_sum < result:
            max_sum = result
        if min_sum > result:
            min_sum = result
        final = max_sum - min_sum

    print(f"#{tc} {final}")
'''
