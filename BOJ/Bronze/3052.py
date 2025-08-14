def div(A,B):
    return A % B


T = 10

result = []
for _ in range(T):
    N = int(input())
    nameoji = div(N,42)
    result.append(nameoji)
cnt = [0] * 42
for i in result:
    cnt[i] += 1
count = 0
for x in cnt:
    if x > 0:
        count += 1
    
print(count) 

'''set사용
division = set()
for _ in range(10):
    N= int(input())
    division.add(N%42)

print(len(division))
'''