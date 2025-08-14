str = input().strip()

result = []

for i in str:
    if 'a' <= i <= 'z':
        # print(chr(ord(i)-32))
        result.append(chr(ord(i)-32))  # 아스키 코드 A는 65 a는 97
    else:
        # print(chr(ord(i)+32))
        result.append(chr(ord(i)+32))

print(''.join(result))

print(*result, sep='') # end 는 무조건 끝에만!