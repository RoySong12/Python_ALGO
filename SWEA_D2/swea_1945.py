# T = int(input())

# sum_a = 0
# sum_b = 0
# sum_c = 0
# sum_d = 0
# sum_e = 0

# for tc in range(1, T+1):
#     N = int(input())
#     if N / 2 >= 1:
#         sum_a = sum_a + N


T = int(input())
ele = [2,3,5,7,11]

for tc in range(1, T+1):
    N = int(input())
    result=[]

    for i in ele:
        count_ele = 0
        while N % i == 0:
            N = N // i
            count_ele += 1
        result.append(count_ele)
    # a,b,c,d,e = result
    # print(f"#{tc}", a,b,c,d,e)
    print(f"#{tc}", *result)