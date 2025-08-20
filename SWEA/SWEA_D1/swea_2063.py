N = int(input())

arr = list(map(int, input().split()))

lst = sorted(arr)  
'''list.sort()는 원본 리스트 직접 변경
sorted()는 원본은 그대로 정렬된 새 리스트 반환
''' 
result = lst[N // 2]

print(result)



'''8/6
N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

middle = N // 2

print(numbers[middle])
'''