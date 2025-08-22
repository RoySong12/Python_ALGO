# i = 1
# while True:
#     r, w, l = map(int, input().split())
#     if (w ** 2 + l ** 2) ** 0.5 <= 2 *r:
#         print(f"Pizza {i} fits on the table.")
#     else:
#         print(f"Pizza {i} doesn not fit on the table.")
#     i += 1
#     if r==0 and  w == 0 and l == 0:
#         break

import sys

i=1

while(1):
    List=list(map(int,sys.stdin.readline().split()))

    if List[0]==0:
        break
    else:
        r,w,l=List

    num=(w/2)**2 + (l/2)**2

    if r**2 >= num:
        print(f"Pizza {pizza} fits on the table.")
    else: 
        print(f"Pizza {pizza} does not fit on the table.")

    pizza=pizza+1