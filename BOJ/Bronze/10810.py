N, M = map(int, input().split())
counts= [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        counts[x] = k
print(*counts, sep=' ')


# N, M = map(int, input().split())
# a = [0] * N

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     a[i-1:j] = [k] * (j - (i - 1))

# print(*a)
