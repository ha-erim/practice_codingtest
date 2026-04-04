### 시간초과 ###
'''
stack = []
top = -1

count = int(input())

for i in range(count):
    command = input()
    if ' ' in command:
        com, num = command.split()
        if com == "push":
            stack.append(num)
            top = num
            # print(f"stack: {stack}, top: {top}")
    
    if command == "top":
        print(top)
        
    
    if command == "size":
        print(len(stack))
    
    if command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    if command == "pop":
        if top == -1:
            print(-1)
            # print(f"stack: {stack}, top: {top}")
        else:
            print(stack.pop())
            if len(stack) != 0:
                top = stack[len(stack)-1]
                # print(f"stack: {stack}, top: {top}")
            else:
                top = -1
'''

import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        _, num = command.split()
        stack.append(num)

    elif command == "pop":
        print(stack.pop() if stack else -1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        print(0 if stack else 1)

    elif command == "top":
        print(stack[-1] if stack else -1)