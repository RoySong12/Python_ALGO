total = 0
prev = 0
for i in range(10):
    N = int(input())
    prev = total
    total += N
    if total >= 100:
        if abs(100 - prev) < abs(100 - total):
            print(prev)
        else:
            print(total)
        break
else:
    print(total)



