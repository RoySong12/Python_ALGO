for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    #행의 합
    row_max = max(sum(row) for row in arr)
    #열의 합
    column_max = max(sum(arr[i][j] for i in range(100)) for j in range(100))
    #대각선 우하단 내려가기
    diag1_max = sum(arr[i][i] for i in range(100))
    #대각선 좌하단 내려가기
    diag2_max = sum(arr[i][99-i] for i in range(100))

    result = max(row_max, column_max, diag1_max, diag2_max)

    print(f"#{tc} {result}")