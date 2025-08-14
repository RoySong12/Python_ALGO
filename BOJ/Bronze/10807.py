N = int(input())

str = map(int, input().split())

M = int(input())

count = 0
for i in str:
    if i == M:
        count += 1
print(count)