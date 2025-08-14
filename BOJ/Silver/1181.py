N = int(input())



words = set()
for _ in range(1, N+1):
    M = input().strip()
    words.add(M) #set 함수에는 append가 아니라 add를 써야한다

sorted_words = sorted(words, key = lambda x: (len(x), x))


for w in sorted_words:
    print(w)



'''버블 정렬
N = int(input())

words = set()
for _ in range(N):
    M = input().strip()
    words.add(M)  # 중복 제거

words = list(words)  # 정렬 위해 리스트 변환

def compare(a, b):
    """a가 b보다 앞서야 하면 True, 아니면 False 반환"""
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    else:
        return a < b  # 길이 같으면 사전순 비교

# 버블 정렬 구현
for i in range(len(words) - 1):
    for j in range(len(words) - 1 - i):
        if not compare(words[j], words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]

for w in words:
    print(w)
'''