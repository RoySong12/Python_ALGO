T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = input().strip()           # N개의 숫자가 붙어서 주어짐

    counts = [0] * 10                  # 0~9 등장 횟수 카운터
    for i in data:
        counts[int(i)] += 1           # 해당 숫자 인덱스에 1씩 추가

    max_cnt = 0
    max_num = 0
    for i in range(10):
        # 등장 횟수가 같으면 더 큰 i를 선택하기 위해 >= 사용
        if counts[i] >= max_cnt:
            max_cnt = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')