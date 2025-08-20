str1 = "XYPV"
str2 = "EOGGXYPVSY"

max_cnt = 0

for ch in set(str1):
    cnt = 0
    for c in str2:
        if ch == c:
            cnt += 1
    print(cnt)