str1 = "XYPV"
str2 = "EOGGXYPVSY"

max_cnt = 0
max_char = ''

for ch in set(str1):
    cnt = 0
    for c in str2:
        if ch == c:
            cnt += 1
    print(ch, cnt)

    if max_cnt < cnt:
        max_cnt = cnt
        max_char = ch
print('--')
print(max_char, max_cnt)