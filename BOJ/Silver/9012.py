T = int(input())
for _ in range(T):
    s = input()
    stack = []
    ok = True
    for ch in s:
        if ch == '(':
            stack.append('(')      # push
        else:  # ch == ')'
            if not stack:         #스택 비어있는데 ')'이걸로 시작하면 바로 잘못된 문자열
                ok = False
                break
            stack.pop()            # pop
    # 모두 처리 후 스택이 비어 있어야 올바른 VPS
    print("YES" if ok and not stack else "NO")





T = int(input())
for _ in range(T):
    s = input()
    stack = []
    ok = True
    for i in s:
        if i == '(':
            stack.append('(')
           
        else:
            if not stack:
                ok = False
                break
                
            stack.pop()
    print("YES" if ok and not stack
           else "NO")