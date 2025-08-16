T = int(input())


for tc in range(1, T+1):
    N = int(input())
    list = list(map(int, input().split()))
    
    special = []

    for k in range(10):
        idx = 0
        if k % 2 == 0:
            for i in range(1, len(list)):
                if list[i] > list[idx]:
                    idx = i
        else:
            for i in range(1, len(list)):
                if list[i] < list[idx]:
                    idx = i
        special.append(list[idx])
        list.pop(idx)

    print(f"#{tc}" , *special)

