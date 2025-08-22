N = int(input())

stack = []
out = []

for _ in range(N):
    M = input().split()

    if M[0] == "push":
        stack.append(int(M[1]))
    elif M[0] == "pop":
        out.append(str(stack.pop()) if stack else "-1")
    elif M[0] == "size":
        out.append(str(len(stack)))
    elif M[0] == "empty":
        out.append("0" if stack else "1")
    elif M[0] == "top":
        out.append(str(stack[-1]) if stack else "-1")

print("\n".join(out))


