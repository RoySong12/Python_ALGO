N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []

for a in A:
    if a < X:
        result.append(a)
print(*result)


