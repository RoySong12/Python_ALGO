T = int(input())

for tc in range(1, T+1):
    N , arr = input().split()
    N = int(N)
    result = []

    for i in arr:
        result.append(N * i)
    print(''.join(result))
'''
그냥 문자열을 리스트로 안받아도 문자열 자체가 반복 가능한 개체 이터러블이기 때문에 for문으로 순회 가능
'''