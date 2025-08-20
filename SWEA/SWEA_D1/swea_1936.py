A, B = map(int, input().split())

if (A == 1 and B == 3) or ( A ==2 and B == 1) or (A == 3 and B == 2):
    print("A")
else:
    print("B")


'''8/6
A, B = map(int, input().split())

if A < B:
    print('B')
    if A == 3 and B == 1:
        print('A') 
else:
    print('A')
    if B == 3 and A ==1:
        print('B')
'''



A, B = map(int, input().split())

if (A==1 and B == 2) or (A==2 and B==3) or (A==3 and B==1):
    print('B')
else:
    print('A')