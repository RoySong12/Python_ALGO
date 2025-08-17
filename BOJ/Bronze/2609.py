def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a  #최대 공약수



N, M = map(int, input().split())

g = gcd(N, M)
l = N * M // g #최소 공배수

print(g)
print(l)

