T = int(input().strip())
for tc in range(1, T + 1):
    E, N = map(int, input().split())

    nums = []
    while len(nums) < 2 * E:
        nums += list(map(int, input().split()))

    children = {}
    for i in range(0, 2 * E, 2):
        p, c = nums[i], nums[i + 1]
        children.setdefault(p, []).append(c)

    
    stack = [N]
    cnt = 0
    while stack:
        u = stack.pop()
        cnt += 1
        if u in children:
            stack.extend(children[u])

    print(f"#{tc} {cnt}")
