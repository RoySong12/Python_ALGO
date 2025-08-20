# T = int(input())

# for i in range(1, T +1):
#     N, hex_str = input.split()
#     binary_part=[]

#     for hx in hex_str:
#         binary_part.append(bin(int(hx, 16))[2:].zfill(4))
#     result=''.join(binary_part)
#     print(f"#{i} {result}")



T = int(input())

for i in range(1, T +1):
    N, M = input().split()
    binary_parts=[]


    for ch in M:
        binary_parts.append(bin(int(ch, 16))[2:].zfill(4))
    result =''.join(binary_parts)
    print(f"#{i} {result}")