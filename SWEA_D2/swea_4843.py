T = int(input())


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    special = []

    for k in range(10):
        idx = 0
        if k % 2 == 0:
            for i in range(1, len(lst)):
                if lst[i] > lst[idx]:
                    idx = i
        else:
            for i in range(1, len(lst)):
                if lst[i] < lst[idx]:
                    idx = i
        special.append(lst[idx])
        lst.pop(idx)

    print(f"#{tc}" , *special)

