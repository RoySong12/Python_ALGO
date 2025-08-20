T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    total = sum(arr[1:9])
    
    result = round(total / 8)
    print(f"#{i} {result}")