T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    heap = [0]

    for num in arr:
        heap.append(num)
        idx = len(heap) -1
        while idx[num] > idx[num+1]:

###아직 풀 단계 아님