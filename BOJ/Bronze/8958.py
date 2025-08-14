N = int(input())

for _ in range(1, N+1):
    S = input().strip()

    score = [0] * 80
    for i in S:
        if S[i] == S[i+1]:
            score[i] += 1
        elif S[i] != S[i+1]:
            score[i+1] = 0
    print(sum(score))


T = int(input())

for _ in range(T):
    s = input().strip()
    run = 0      # 현재 연속 O의 길이
    total = 0    # 총점
    for ch in s:
        if ch == 'O':
            run += 1
            total += run
        else:          # ch == 'X'
            run = 0
    print(total)
