Notes = map(int, input().split())

for i in Notes:
    if i < i+1:
        print("ascending")
    elif i > i+1:
        print("descending")
    else:
        print("mixed")