N = int(input())
letter = input()

if letter[-1] == 'G':
    letter = letter[:-1]
else:
    letter = letter +'G'


print(letter)