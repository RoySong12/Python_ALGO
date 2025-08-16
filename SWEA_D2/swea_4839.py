def binary_search(P, key):
    l, r = 1, P # 왼쪽 오른쪽 첫 페이지 마지막페이지로 설정
    cnt = 0
    while 1 <= r:
        cnt += 1 
        c = (1+r) //2 #중간값
        if c == key:
            return cnt
        elif c > key:
            r = c
        else:
            l = c
    return cnt

T = int(input())

for tc in range(1, T+1):
    P,Pa,Pb = map(int, input().split())

    A =binary_search(P,Pa)
    B = binary_search(P, Pb)

    if A < B:
        print(f"#{tc} A")
    elif B < A:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")
