N = int(input())
M1 = set(map(int, input().split()))
N1 = int(input())
M2 = list(map(int, input().split()))
for i in M2:
    if i in M1:
        print('1')
    else:
        print('0')