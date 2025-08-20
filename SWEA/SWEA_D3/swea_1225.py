for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))

    minus = 1

    while True:
        x = nums.pop(0) - minus
        if x <= 0:
            nums.append(0)
            break
        nums.append(x)
        minus += 1
        if minus == 6:
            minus =1

    print(f"#{tc} {' '.join(map(str, nums))}")
