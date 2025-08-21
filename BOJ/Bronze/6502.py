i = 1
while True:
    r, w, l = map(int, input().split())
    if (w ** 2 + l ** 2) ** 0.5 <= 2 *r:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} doesn not fit on the table.")
    i += 1
    if r==0 and  w == 0 and l == 0:
        break


# import sys

# i = 1
# for line in sys.stdin:
#     r, w, l = map(int, line.split())
#     if r==0 and  w == 0 and l == 0:
#         break


#     if (w ** 2 + l ** 2) ** 0.5 <= 2 *r:
#         print(f"Pizza {i} fits on the table.")
#     else:
#         print(f"Pizza {i} doesn not fit on the table.")
#     i += 1
    