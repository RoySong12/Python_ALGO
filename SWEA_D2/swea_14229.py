arr = list(map(int, input().split()))
k = 1000000
counts = [0] * (k + 1)
result = [0] * len(arr)
for ele in arr:
    counts[ele] += 1
for idx in range(len(counts) - 1):
    counts[idx + 1] += counts[idx]
for idx in range(len(arr) -1, -1, -1):
    counts[arr[idx]] -= 1
    result[counts[arr[idx]]] = arr[idx]
print(result[500000])






N = list(map(int, input().split()))

k = 1000000

counts = [0] * (k+1)

for i in N:
    counts[i] += 1

ans =500000

idx = 0 
for j in range(k+1):
    if counts[j] > 0:
        if idx + counts[j] > ans:
            print(j)
            break
        idx += count[j]



import sys

def solve():
    input = sys.stdin.readline
    TC = int(input().strip())
    for _ in range(TC):
        N, lo, hi = map(int, input().split())
        scores = list(map(int, input().split()))
        # 혹시 입력이 여러 줄로 나뉠 가능성에 대비 (안전장치)
        while len(scores) < N:
            scores += list(map(int, input().split()))

        # 1) 점수 빈도 (1~100)
        freq = [0] * 101
        for v in scores:
            freq[v] += 1

        # 2) 누적합
        pref = [0] * 101
        for s in range(1, 101):
            pref[s] = pref[s-1] + freq[s]

        ans = None

        # 3) 모든 (score1, score2) 시도
        # score1은 1..99, score2는 score1+1..100
        for s1 in range(1, 100):
            poor = pref[s1-1]  # < s1
            # 미리 범위 체크로 가지치기(부진 분반)
            if not (lo <= poor <= hi):
                # 그래도 score2에 따라 poor는 변하지 않으므로 스킵
                continue

            for s2 in range(s1+1, 101):
                normal = pref[s2-1] - pref[s1-1]     # s1 <= score < s2
                excellent = N - pref[s2-1]           # >= s2

                if lo <= normal <= hi and lo <= excellent <= hi:
                    mx = max(poor, normal, excellent)
                    mn = min(poor, normal, excellent)
                    diff = mx - mn
                    if (ans is None) or (diff < ans):
                        ans = diff

        print(ans if ans is not None else -1)

if __name__ == "__main__":
    solve()
