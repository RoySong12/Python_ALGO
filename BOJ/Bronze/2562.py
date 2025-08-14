'''
T = 9

result = []
for _ in range(T):
    N = int(input())
    result.append(N)

result.sort()    #sort를 사용하면 원래 순서 정보가 사라지므로 최댓값 인덱스를 구하려면 max() + index()방법이 안전함.
print(result[-1])
print(idx[result[-1]]+1)
'''


T = 9

result = []
for _ in range(T):
    N = int(input())
    result.append(N)

max_value = max(result)            # 최댓값
print(max_value)                   # 최댓값 출력
print(result.index(max_value) + 1) # 인덱스(1-based) 출력

    