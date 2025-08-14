T = int(input())

for i in range(1, T+1):
    N, S = input().split()
    S = int(S)

    if 97 <= S <= 100:
        print(N, 'A+')
    elif 90 <= S <= 96:
        print(N, 'A')
    elif 87 <= S <= 89:
        print(N, 'B+')
    elif 80 <= S <= 86:
        print(N, 'B')
    elif 77 <= S <= 79:
        print(N, 'C+')
    elif 70 <= S <= 76:
        print(N, 'C')
    elif 67 <= S <= 69:
        print(N, 'D+')
    elif 60 <= S <= 66:
        print(N, 'D')
    else:
        print(N, 'F')    