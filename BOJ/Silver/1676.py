N = int(input())


fact = 1
for i in range(1, N +1):
    fact *= i

lst = str(fact)

cnt = 0
for j in reversed(lst):
    if j == 0:
        cnt += 1
    else:
        break
print(cnt)







N = int(input())


fact = 1
for i in range(1, N +1):
    fact *= i

lst = str(fact)

cnt = 0
for j in lst[::-1]: #역순으로 복사한 새 객체 만들어줌.
    if j == '0':
        cnt += 1
    else:
        break
print(cnt)