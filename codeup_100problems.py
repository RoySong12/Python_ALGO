#6001
print("Hello")

#6002
print("Hello World")

#6003
print("Hello\nWorld")

#6004
print("'Hello'")        

#6005
print('"Hello World"')

#6006
print('"!@#$%^&*()\'')

#6007
print('"C:\\Download\\\'hello\'.py"')

#6008
print('print("Hello\\nWorld")')

#6009
a = input()
print(a)

#60010
a= int(input())
print(a)

#60011
a =float(input())
print(a)

#60012
a =int(input())
b = int(input())

print(a)
print(b)

#60013
a = input()
b = input()         
print(b)
print(a)

#60014
a = float(input())
print(a)
print(a)
print(a)

#60015
a, b = map(int,(input().split()))
print(a)
print(b)

#60016
a, b = input().split()
print(b,a)

#60017
a = input()
print(a,a,a)

#60018
a,b = input().split(':')
print(a,b,sep=':')

#60019
y, m, d = input().split('.')
print(d, m, y, sep='-')

#60020
a, b = input().split('-')
print(a, b, sep='')

#60021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#60022
s = input()
print(s[0:2], s[2:4], s[4:])

#60023
a,b,c = input().split(':')
print(b)

#60024
a,b=input().split()
c=a+b
print(c)

#60025
a, b = input().split()
print(int(a) + int(b))

#60026
a = float(input())
b = float(input())
print(a + b)

#60027
a = input()
n = int(a)
print('%x'% n)

#60028
a = input()
n= int(a)
print('%X' %n)  
##name = "진현"
##print("안녕하세요, %s님!" % name)

### 파이썬 3.6이상에서는 f-string을 사용할 수 있습니다.
###예시 print(f"안녕하세요, {name}님!")
###다른 풀이 print(f"{n:X}") 

#60029
a=input()
n=int(a,16)
print(f"{n:O}")

a = input()
n= int(a,16)
print('%o' %n)  

#60030
n = ord(input())
print(n)

#60031
n = int(input())
print(chr(n))

#60032
n = int(input())
print(-n)

#60033
n = input()
print(chr(ord(n) + 1)) #ord(n):문자를 유니코드 숫자로 변환 #chr(--): 다시 숫자를 문자로 변환

#60037
n = input()
str = input()
print(str * int(n))

#6038
a, b = map(int, input().split())
print( a ** b)

#6039
a, b = map(float, input().split())
print(a ** b)

#6040
a, b = map(int, input().split())
print(a // b)

#6041
a, b = map(int, input().split())    
print(a % b)

#6042
a = float(input())
print(format(a, ".2f"))
print(f"{a:.2f}")

#6043
f1, f2 = map(float, input().split())
print(f"{f1 / f2:.3f}")

#6044
a, b = map(int, input().split())
print(a +b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(f"{a / b:.2f}")

#6045
a,b,c =map(int, input().split())
print(a+b+c, f"{(a+b+c) / 3:.2f}")

#6046
a =int(input())
print(a<<1)

#6047
a, b =map(int, input().split())
print(a * 2**b)

#6048
a, b =map(int, input().split())
print(a < b)

#6049
a, b = map(int, input().split())
print(a==b)

#6050
a, b = map(int, input().split())
print( a <= b)

#6051
a, b = map(int, input().split())
print( a!= b)

#6052
a = int(input())
if a == 0:
    print("False")
else: 
    print("True")

# n = int(input())
# print(bool(n))

#6053
a = bool(int(input()))
print(not a)

# n= int(input())
# print(n==0)


#6054
a, b = map(int, input().split())
print(bool(a) and bool(b))


#6055
a, b = map(int, input().split())
print(bool(a) or bool(b))

#6056
a, b = map(int, input().split())
print((bool(a) and not bool(b)) or (bool(b) and not bool(a)))

#6057
a, b = map(bool, map(int, input().split()))
print((a and b) or (not a and not b))

#6058
a, b = map(bool, map(int, input().split()))
print(not(a or b))

#6059
a = int(input())
print(~a)

###~n = -(n+1) #n이 음수일 때, n의 2의 보수 표현을 구하는 방법

#6060
a, b = map(int,(input().split()))
print(a & b)

#6061
a, b = map(int,(input().split()))
print(a | b)

#6062
a, b = map(int,(input().split()))
print(a ^ b)

#6063
a, b = map(int,(input().split()))
if a > b:
    print(a)
else:
    print(b)
#6064
a, b ,c = map(int,(input().split()))
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else: 
    print(c)
'''
a, b, c = map(int, input().split())
print(min(a, b, c))
'''

#6065
a, b, c = map(int,(input().split()))

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

#6066
a, b, c = map(int,(input().split()))
if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

#6067
n = int(input())
if n<0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')

#6068
point = int(input())
if point >= 90:
    print('A')
elif point >= 70:
    print('B')
elif point >=40:
    print('C')
else:
    print('D')

#6069
alphabet = input()

if alphabet == 'A':
    print('best!!!')
elif alphabet == 'B':
    print('good!!')
elif alphabet == 'C':
    print('run!')
elif alphabet == 'D':
    print('slowly~')
else:
    print('what?')

#6070
month = int(input())
# if month 3<= and 5>=:


if month // 3 == 1:
    print("spring")
elif month // 3 == 2:
    print("summer")
elif month // 3 == 3:
    print("fall")
else:
    print("winter")

