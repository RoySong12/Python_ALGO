# N = int(input())


# asc = []
# for i in range(N):
#     I = int(input())
#     asc.append(I)
# result = sorted(asc)

# print(*result, ) # 한줄 한줄 출력하려면 무조건 for문을 돌아야 하기 때문에 이 방식은 틀림.


'''
N = int(input())
nums = [int(input()) for _ in range(N)]
print(*sorted(nums))
'''


#제일깔끔
N = int(input())

nums = [int(input()) for _ in range(N)]
for num in sorted(nums):
    print(num)


