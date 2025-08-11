T = int(input())

for i in range(1, T+1):
    str1 = input()
    str2 = input()

    counts={}

    for ch in str2: # 긴 문자열에서 문자를 하나씩 꺼내서
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    # print(counts)

    max_val = 0
    for ch in str1: #짧은 문자열에서 카운트가 많은 문자 추출
        if ch in counts:
            # print(ch, counts[ch])
            if max_val < counts[ch]:
                max_val = counts[ch]
    
    print(f"#{i} {max_val}")


    input().strip() # 혹시나 문자열 양 옆에 공백이 있으면 공백 제거


'''8/6
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_num = 0

    for i in str1:
        count = str2.count(i)
        if count > max_num:
                max_num = count
                
    print(f"#{tc} {max_num}")
'''


'''test
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
'''