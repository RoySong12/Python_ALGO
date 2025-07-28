T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    max_num = numbers[-1]
    print(f"#{i} {max_num}")