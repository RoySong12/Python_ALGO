T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
 
    for i in range(N-1):
        min_i = i
        for j in range(i+1, N):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
 
    print(f"#{tc}", *arr)



# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))

#     for i in range(N-1):
#         min_i = i
#         for j in range(i+1, N):
#             if lst[j] < lst[min_i]:
#                 min_i = j
#         lst[i], lst[min_i] = lst[min_i], lst[i]

#     print(f"#{tc}", *lst)