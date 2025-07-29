#ws_1_a
print("안녕하세요")


#ws_1_b
korean = "한글"
english = "english"
number = 3

print(f"{korean}과 {english}")
print(korean * number)

#ws_1_c
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.

first_char = password[28:36]
second_word = password[113:118]
third_word = password[68:65:-1]
fourth_word = password[325:321:-1]
fifth_word = password[365:371]

print(f'{first_char}{second_word} {third_word} {fourth_word} "{fifth_word}".')

#ws_1_1
n = '홍길동'
a = 20
s = '이름 : '
s2 = '나이 : '
s3 = '학생 정보를 출력합니다.'
s4 = '각각의 정보는 다음과 같습니다'
s5 = '출력 완료'

print(s3)
print(s4)
print(s,n)
print(s2,a)
print(s5)

#ws_1_2
string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))


#ws_1_3
# main.py

a = '반짝 반짝'
b = '에서도'
c = '작은별'
d = '아름답게 비치네'
e = '동쪽 하늘'
f = '서쪽 하늘'

print(f"{a} {c[:2]} {c[2]} {d}")
print(f"{e}{b} {f}{b}")
print(f"{a} {c[:2]} {c[2]} {d}")


#ws_1_4
# 원주율
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
r = 15

print(f"원주율 : {pi:.15f}")
print(f"반지름 : {r}")
print(f"원의 둘레 : {2*pi*r:.14f}")
print(f"원의 넓이 : {pi**2*r:.14f}")


#ws_1_5
print(3*2)
print(3**2)
print((3**2)//(3*2),(3**2)%(3*2))
print((3**2)+((-3)**2))

#hw_1_4

# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi

apple = "사과는 영어로 apple "
banana = "바나나는 영어로 banana"
kiwi = "키위는 영어로 kiwi"

print(apple)
print(banana)
print(kiwi)