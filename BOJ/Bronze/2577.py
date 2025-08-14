A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)


for i in range(10):
    print(result.count(str(i)))


''' 내장 함수 없이!!!
A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
counts = [0] * 10

for i in result:
    counts[int(i)] += 1

for cnt in counts:
    print(cnt)
'''