def Water(A,X,B):
    return A* (X-1) +B
    
N = int(input())
for i in range(N):
    A, B, X = map(int, input().split())
    print(Water(A,X,B))

# N = int(input())

# for _ in range(N):
#     A, B, X = map(int, input().split())
#     result = (A * (X-1) + B)
#     print(result)


