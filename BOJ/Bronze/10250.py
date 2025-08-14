          
T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())

    floor = N % H
    room = (N // H) + 1
    if floor == 0 :
        floor = H
        room = room -1

    print(f"{floor}{room:02d}")
