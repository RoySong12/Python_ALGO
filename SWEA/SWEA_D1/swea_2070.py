T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        print(f"#{i} '<'")
    elif a = b:
        print(f"#{i} '='")
    else:
        print(f"#{i} '>'")


'''
T = int(input())

for i in range(1, T+1):
    a,b = map(int, input().split())
    if a < b:
        result = "<"
    elif a > b:
        result = ">"
    else:
        result = "="
    print(f"#{i} {result}")
'''


#8/5
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     if N > M:
#         result = '>'

#     elif N < M:
#         result = '<'
#     else:
#         result = '='
    
#     print(f"#{tc} {result}")



