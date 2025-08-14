notes = list(map(int, input().split()))

asc = True
desc = True

for i in range(len(notes) - 1):
    if notes[i] < notes[i+1]:
        desc = False
    elif notes[i] > notes[i+1]:
        asc = False

if asc:
    print("ascending")
elif desc:
    print("descending")
else:
    print("mixed")




'''sorted사용
notes = list(map(int, input().split()))

if notes == sorted(notes):
    print("ascending")
elif notes == sorted(notes, reverse=True):
    print("descending")
else:
    print("mixed")


sorted()함수는 원본 리스트 변경하지 않고 정렬된 새 리스트 반환

list.sort()메서드는 리스트 객체 전용으로 원본 리스트를 직접 정렬

이 문제는 기존 리스트와 정렬된 리스트를 비교해야하기 때문에 sorted함수가 적절.





ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
notes = list(map(int, input().split()))
print("ascending" if notes == sorted(notes) else "descending" if notes == sorted(notes, reverse=True) else "mixed")

'''