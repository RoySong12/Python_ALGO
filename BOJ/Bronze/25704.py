N = int(input())
P = int(input())

ans = [P]

if N >= 5:
    ans.append(P - 500)
if N >= 10: 
    ans.append(int(P * 0.9))
if N >= 15:
    ans.append(P - 2000)
if N >= 20:
    ans.append(int(P * 0.75))
    

print(max(min(ans),0))