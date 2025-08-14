# A = int(input())
# B = int(input())
# C = int(input())

# number = A + B - C
# string_left = str(A) + str(B) 
# string_right = str(c)

# result = int(string_left) - int(string_right)

# print(number)
# print(result)



# BOJ 31403: A + B - C
A = input().strip()   # 문자열로 받기
B = input().strip()
C = input().strip()

# 1) 숫자로 계산
print(int(A) + int(B) - int(C))

# 2) 문자열 이어붙인 뒤 숫자로 변환해 계산
print(int(A + B) - int(C))
