T = int(input())


for tc in range(1, T+1):

    n, k = map(int, input())

    pixel = n + 3

    count = [0] * (pixel + 1)


    for t in range(1, k+1):
        for s in range(t, pixel +1, t):
            count[s] += 1
    

    result = 0
    for i in range(n):
          for j in range(4):
                S = i + j + 1
                if count[S] % 2 == 1
                result += 1

    print(f"#{tc} {result}")