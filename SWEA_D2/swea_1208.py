for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    for _ in range(N):
        max_idx = height.index(max(height))
        min_idx = height.index(min(height))

        height[max_idx] -= 1
        height[min_idx] += 1

    result = max(height) - min(height)
    print(f"#{tc} {result}")


for tc in range(1, 11):
    D = int(input())
    arr = list(map(int, input().split()))


    for _ in range(D):
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1

    result = max(arr) - min(arr)
    print(f"#{tc} {result}")