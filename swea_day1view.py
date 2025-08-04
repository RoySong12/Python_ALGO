for i in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    view_sum = 0

    for j in range(2, N-2):

        neighbors = [
            height[j-2],
            height[j-1],
            height[j+1],
            height[j+2],
        ]
        # sec_max = max(neighbors)

        # 최댓값을 찾으려면 최소값으로 초기화하고
        # 최소값을 찾으려면 최대값으로 초기화한다.

        sec_max = neighbors[0] # 첫번째값이 있다면 그걸 쓰면됨
        sec_max = 0 # 최소값으로 초기화
        for neighbor in neighbors:
            if neighbor > sec_max:
                sec_max = neighbor


        if height[j] > sec_max:
            view_sum = view_sum + (height[j]-sec_max)
    print(f"#{i} {view_sum}")



        