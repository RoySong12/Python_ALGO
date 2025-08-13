def scoring(A, B, C, D, E):
    score = (6*A) + (3*B) + (2*C) + (1*D) + (2*E)
    return score

A,B,C,D,E = list(map(int, input().split()))

a,b,c,d,e = list(map(int, input().split()))

print(scoring(A,B,C,D,E), scoring(a,b,c,d,e))
