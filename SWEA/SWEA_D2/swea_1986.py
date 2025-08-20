T = int(input())

for i in range(1, T+1):
    N = int(input())
    num_list = list(range(1, N+1))
    plus = []
    minus = []
    for n in num_list:
        if n % 2 == 0:
            minus.append(n)
        else:
            plus.append(n)
    result = sum(plus) - sum(minus)

    print(f"#{i} {result}")




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # i가 짝수면 +i, 홀수면 –i
    result = sum(i if i % 2 == 0 else -i for i in range(1, N+1))
    print(f"#{tc} {result}")







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = N // 2
    result =  m if N % 2 == 0 else -(m + 1)
    print(f"#{tc} {result}")