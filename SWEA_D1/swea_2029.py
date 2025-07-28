T = int(input())


for i in range(1, T+1):
    a, b = map(int, input().split())
    main = a // b
    sub = a % b
    print(f"#{i} {main} {sub}")




