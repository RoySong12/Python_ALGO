T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    result = round(avg)
    print(f"#{i} {result}")


'''
T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    result = round(avg)
    print(f"#{i} {result}")
'''