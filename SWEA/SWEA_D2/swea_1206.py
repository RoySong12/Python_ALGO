for i in range(1, 11):
    N=int(input())
    height = list(map(int, input().split()))

    view_sum=0

    for j in range(2, N-2):
        neighbors = [
            height[j-2],
            height[j-1],
            height[j+1],
            height[j+2],
        ]
        sec_max = neighbors[0]

        for neighbor in neighbors:
            if neighbor > sec_max:
                sec_max = neighbor
        
        if height[j] > sec_max:
            result = height[j] - sec_max
            view_sum = view_sum + result
    print(f"{i} {view_sum}")






for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    view_sum = 0
    for i in range(2, N-2):
        neighbors = [
            buildings[i-2],
            buildings[i-1],
            buildings[i+1],
            buildings[i+2],
        ]
        sec_max = neighbors[0]

        for neighbor in neighbors:
            if neighbor > sec_max:
                sec_max = neighbor
        if buildings[i] > sec_max:
            result = buildings[i] - sec_max
            view_sum += result
    print(f"#{tc} {view_sum}")
                     

 






