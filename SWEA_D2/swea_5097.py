'''8/6
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input().split())
    ans = M % N

    result = arr[ans]

    print(f"#{tc} {result}")
'''


T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    idx = M % N
    answ = arr[idx]
    print(f"#{i} {answ}")
