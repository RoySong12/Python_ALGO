T = int(input())


for i in range(1, T+1):
    numbers = map(int, input().split())
    total = 0
    for num in numbers:
        if num % 2 ==1:
            total += num
    print(f"#{i} {total}")