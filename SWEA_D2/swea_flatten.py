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