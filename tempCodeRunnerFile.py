T = int(input())

for i in range(1, T+1):
    str1 = input()
    str2 = input()


    counts=[]
    for ch in str2:
        if ch in counts:
            counts[ch] += counts + 1
        else:
            counts[ch] = 1
    print(counts)
