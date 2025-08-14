T = int(input())

for tc in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))


    counts = [0] * 101
    for i in scores:
        counts[i] += 1

    results = [0] * 101    #누적합
    for j in range(1, 101):
        results[j] = results[j-1] + counts[i]


    min_v = 999999999999999999

    for s1 in range(1, 101):
        bad = results[s1 - 1]
        if not (min <= bad <= max):
            continue
        for s2 in range(s1 + 1, 101):
            normal = results[s2 -1] - results[s1 - 1]
            good = N - results[s2 - 1]

        if min <= normal <= max and min <= good <= max:
            mx = max(bad, normal, good)
            mn = min(bad, normal, good)
            diff = mx - mn
            if diff < min_v:
                min_v = diff
    

    for s1 in range(1, 101):
        for s2 in range(s1, 101):
            bad = results[s1 - 1]
            normal = results[s2-1] - results[s1 - 1]
            good = N - results[s2 -1]
            if min<=bad<=max and min <= normal <= max and min <= good <= max:


#score1, score2
#=> 3개 분반으로 나누기
# min <= 각 분반의 학생 수 <=max
# 3개 분반 중에서 가장 많은 분반 - 가장 적은 분반은 최소


#완전 탐색--->최솟값
#모든 경우의 수를 전부 만든 다음 => 조건에 맞는 것들 검사 => 그 중 최소값, 최댓값 찾기


T = int(input())

for tc in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))

    min_val = 9999999999 #인원 수 차이의 최댓값

    for score1 in range(1, 101):
        for score2 in range(score1, 101):

            cls_cnt = [0]*3 #cls__cnt[0] 부진, 1 보통,  2우수


            for score in scores:
                if score < score1:
                    cls_cnt[0] += 1
                elif score < score2:
                    cls_cnt[1] += 1
                else:
                    cls_cnt[2] += 1


            for i in range(3):
                if cls_cnt[i] < min or cls_cnt[i] > max: 
                    break
            else: #for문을 돌면서 break 안 만난 상황
                #모두 다 범위 안에 있음.
                max_cnt = 0
                min_cnt = 99999999999999
                for i in range(3):
                    if cls_cnt[i] > max_cnt:
                        max_cnt = cls_cnt[i]
                    if cls_cnt[i] < min_cnt:
                        min_cnt = cls_cnt[i]
                diff = max_cnt - min_cnt
                if diff < min_val:
                    min_val = diff


    if min_diff == 999999999999:
        print(f"#{tc} -1")

    print(f"#{tc} {min_val}")


            
'''영주님 풀이
t = int(input())

for pronum in range(t):
    n, min_class, max_class = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()
    min_score = a[0]
    max_score = a[-1]

    delta = -1
    for min_line in range(min_score, max_score + 1):
        for max_line in range(min_score, max_score + 1):
            k1 = 0
            k2 = 0
            k3 = 0
            for i in a:
                if i >= max_line:
                    k3 += 1
                elif i < min_line:
                    k1 += 1
                else:
                    k2 += 1
            if (
                min_class <= k1 <= max_class
                and min_class <= k2 <= max_class
                and min_class <= k3 <= max_class
            ):
                if delta == -1:
                    delta = max(k1, k2, k3) - min(k1, k2, k3)
                else:
                    if (max(k1, k2, k3) - min(k1, k2, k3)) < delta:
                        delta = max(k1, k2, k3) - min(k1, k2, k3)

    print(f"#{pronum+1} {delta}")
'''