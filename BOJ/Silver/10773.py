K = int(input())



zero = []
for _ in range(K):
    N = int(input())
    if N == 0:
        zero.pop()
    else:
        zero.append(N)
    
result = sum(zero)
print(result)
    