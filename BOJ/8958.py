N = int(input())

for n in range(1, N+1):
    S = input().strip()

    score = [0] * 80
    for i in S:
        if S[i] == S[i+1]:
            score[i] += 1
        elif S[i] != S[i+1]:
            score[i+1] = 0
    print(sum(score))


    