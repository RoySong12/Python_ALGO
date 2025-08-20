#num = 456789
num = int(input())
c = [0] * 12    # c[10], c[11]은 항상 0, run확인을 위한 여분

for _ in range(6):  # 단순 반복 6회
    c[num%10] += 1  # num%10 1의 자리 알아내기
    num //= 10      # num의 1의 자리 제거

i = 0
tri = run = 0
while i < 10:       # 카드 번호 9까지...
    if c[i] >= 3:   # tri. 확인
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1]>=1 and c[i+2]>=1:    # run 확인
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run+tri==2:
    print('win')
else:
    print('lose')



# for i1 in range(1,4):
# 	for i2 in range(1,4):
# 		if i2 != i1:
# 			for i3 in range(1,4):
# 				if i3 != i1 and i3 != i2:
# 					print(i1, i2, i3)