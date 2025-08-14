# stack=[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())





stack[top] =3

top -= 1    #pop
print(stack[top+1])
top -= 1    #pop
print(stack[top+1])
top -= 1    #pop
print(stack[top+1])
print(stack)





T = int(input())

for _ in range(1, T+1):
    n, k = map(int, input().split())
    count_on = 0

    for col in range(1, n+1):    # 열 번호
        for row in range(1, 5):  # 행 번호 (4행)
            S = col + row
            toggle_count = k // S  # S의 배수 개수
            if toggle_count % 2 == 1:
                count_on += 1

    print(count_on)

