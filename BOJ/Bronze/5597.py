
T = 28
stu = list(range(1,31)) #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for _ in range(T):
    N = int(input())
    if N in stu:
        stu.remove(N)
    
print(*stu) 
#for s in stu:
#   print(s)




'''
all_students = set(range(1, 31))
submitted = set(int(input()) for _ in range(28))
absent = sorted(all_students - submitted)

for s in absent:
    print(s)
'''