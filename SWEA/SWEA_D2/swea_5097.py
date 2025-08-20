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



#강사님 풀이.
#큐를 쓰면 됨
from collections import deque
T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    q = deque() #큐 생성
    q.extend(arr) #arr 수를 모두 큐에 삽입.

    #M번 이동
    for _ in range(M):
        q.append(q.popleft())

    print(f"#{tc} {q.popleft()}")