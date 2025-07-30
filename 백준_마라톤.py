
#백준_2742
N = int(input())

for i in range(N , 0 , -1):
    print(i)


#백준_5522


total = 0
for _ in range(5):
    total = total + int(input())

print(total)


#백준_5337

print(".  .   .")
print("|  | _ | _. _ ._ _  _")
print("|/\|(/.|(_.(_)[ | )(/.")

#백준_9654
# print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
# print("N2 Bomber      Heavy Fighter  Limited    21")
# print("J-Type 327     Light Combat   Unlimited  1")
# print("NX Cruiser     Medium Fighter Limited    18")
# print("N1 Starfighter Medium Fighter Unlimited  25")
# print("Royal Cruiser  Light Combat   Limited    4")


print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
print("N2 Bomber      Heavy Fighter  Limited    21        ")
print("J-Type 327     Light Combat   Unlimited  1         ")
print("NX Cruiser     Medium Fighter Limited    18        ")
print("N1 Starfighter Medium Fighter Unlimited  25        ")
print("Royal Cruiser  Light Combat   Limited    4         ")


#백준_20492

N = int(input())

tax = N * 0.78

tax_neces = N - (N * 0.2 * 0.22)

print(int(tax), int(tax_neces))

#33178

N = int(input())

subject = N // 10 
print(subject)


#2884

H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
else:
    print((H-1) % 24, 60-(45 - M))


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


