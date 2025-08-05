T = int(input())


for i in range(1, T+1):
    numbers = map(int, input().split())
    total = 0
    for num in numbers:
        if num % 2 ==1:
            total += num
    print(f"#{i} {total}")







#8/5
# T = int(input())

# for tc in range(1, T+1):
#     N = map(int, input().split())

#     sum = 0

#     for i in N:
#         if i % 2 == 1:
#             sum +=  i 
#     print(f"#{tc} {sum}")
    

