# T = int(input())

# for tc in range(1, T+1):
#     str1 = input().strip()
#     str2 = input().strip()

    
#     if str1 in str2:
#         print(f"#{tc} 1")
#     else: 
#         print(f"#{tc} 0")



T = int(input().strip())
for tc in range(1, T + 1):
    str1 = input().strip()
    str2 = input().strip()
    
    m, n = len(str1), len(str2)
    found = 0

    if m <= n:
        for i in range(n - m +1):
            j = 0
            while j < m and str2[i + j] == str1[j]:
                j += 1
            if j == m:
                found = 1
                break
    print(f"#{tc} {found}")
