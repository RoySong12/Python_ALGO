T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    max_num = numbers[-1]
    print(f"#{i} {max_num}")




#8/5
# T = int(input())

# for tc in range(1, T+1):
#     N = list(map(int, input().split()))
#     max_num = 0
#     for i in N:
#         max_num = N[0]
#         if max_num < i:
#             max_num = i
#     print(f"#{tc} {max_num}")
