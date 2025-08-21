N = int(input())



elev = [] 
for _ in range(N):
    num = int(input())
    elev.append(num)

elev.sort()

for ele in elev:
    print(ele)


# 시간 초과 해결
# import sys
# input = sys.stdin.readline

# N = int(input())
# elev = [int(input()) for _ in range(N)]

# elev.sort()

# # join으로 한 번에 출력
# sys.stdout.write("\n".join(map(str, elev)))
