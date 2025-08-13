def calculator(A,B):
    result = (A+B)*(A-B)
    return result


A, B = map(int, input().split())

print(calculator(A,B))


