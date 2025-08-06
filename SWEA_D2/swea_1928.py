# T= int(input())

# for tc in range(1, T+1):
#     str = input()
#     div_6 = str[::6]
#     # print(div_6)
#     idx = list(div_6, 64)
#     print(idx)

import base64

T = int(input())

for tc in range(1, T+1):
    str = input().strip()
    decoding = base64.b64decode(str).decode('utf-8')
    print(f"{tc} {decoding}")




base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
T = int(input())

for tc in range(1, T + 1):
    encoded = input()

    # 1. Base64 문자 → 6비트 이진 문자열
    binary = ''
    for i in encoded:
        idx = base64_table.index(i)
        binary += format(idx, '06b')

    # 2. 8비트씩 자르기 → ASCII 문자로 변환
    decoded = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            decoded += chr(int(byte, 2))

    print(f"#{tc} {decoded}")
