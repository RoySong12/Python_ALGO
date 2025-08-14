while True:
    tri = list(map(int, input().split()))
    if tri == [0,0,0]:
        break

    tri.sort() #sorted()와 list.sort차이점 알기

    if (tri[0]**2) + (tri[1]**2) == (tri[2]**2):
        print("right")
    else:
        print("wrong")


'''sorted()다음 리스트가 굳이 안 들어오고 iterable한 문자열, 정수형 문자열(map(int, input().split()))등등 다 올 수 있음
'''



