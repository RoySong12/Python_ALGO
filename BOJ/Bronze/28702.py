lines = [input() for _ in range(3)]


for idx, val in enumerate(lines):
    if val.isdigit():
        n = int(val)
        next_num = n + (3 -idx)
        break

if next_num % 15 == 0:
    print("FizzBuzz")

elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)
    