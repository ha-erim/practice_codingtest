import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = list(sys.stdin.readline().strip())
    stack = []
    VPS = 1
    for a in line:
        if a == "(":
            stack.append('(')
        else:
            if stack:
                flag = stack.pop()
            else:
                VPS = 0
                break
            
    
    if len(stack):
        VPS = 0
    print("YES" if VPS == 1 else "NO")
    