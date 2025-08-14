#14914

a, b = map(int, input().split())

list_a=[]
list_b=[]
for i in range(1, a+1):
    if a % i == 0:
        list_a.append(i)
for j in range(1, b+1):
    if b % j == 0:
        list_b.append(j)
# print(list_a)
# print(list_b)
T=[]
for x in list_a:
    for y in list_b:
        if x == y:
            T.append(x)
T.sort()

for k in T:
    print(k, a // k, b // k)