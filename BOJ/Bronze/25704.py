N = int(input())
price = int(input())



# ans = P

if 5 <= N < 10:
    print(price - 500)
elif 10 <= N < 15:
    print(price * 0.9 )
elif 15 <= N < 20:
    print(price - 2000)
elif 20 <= N:
    print(price * 0.75)
    