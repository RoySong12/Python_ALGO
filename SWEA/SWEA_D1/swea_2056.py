T = int(input())

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]


for i in range(1, T+1):    
    numbers = input().strip()
    year = numbers[:4]
    month = numbers[4:6]
    date = numbers[6:8]

    m = int(month)
    d = int(date)

    if 1 <= m <= 12 and 1<= d <= days_in_month[m]:
         print(f"#{i} {year}/{month}/{date}")

    else:
         print(f"#{i} -1")





'''8/6
T = int(input())

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range(1, T+1):
     N = input()
     year = N[:4]
     month = N[4:6]
     day = N[6:]

     m = int(month)
     d = int(day)


     if 1 <= m <= 12 and 1 <= d <= days_in_month[m]:
          print(f"#{tc} {year}/{month}/{day}")

     else:
          print(f"#{tc} -1")
'''
     

