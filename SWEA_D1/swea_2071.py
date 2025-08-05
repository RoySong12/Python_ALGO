T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    result = round(avg)
    print(f"#{i} {result}")








''' 8/5
T = int(input())


for i in range(1, T+1):
    N = list(map(int, input().split()))

    total = 0
    for j in N:
        total += j
    
    result = round(total / len(N))
    print(f"#{i} {result}")
'''