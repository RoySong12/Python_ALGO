T = int(input())


for i in range(1, T+1):
    a, b = map(int, input().split())
    main = a // b
    sub = a % b
    print(f"#{i} {main} {sub}")



'''8/6
T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    result1 = a // b
    result2 = a % b
    print(f"#{tc} {result1} {result2}")
'''
