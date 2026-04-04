from collections import deque
import sys

n = int(sys.stdin.readline())

deq = deque()

for _ in range(n):
    com = sys.stdin.readline().strip()

    if com.startswith("push"):
        _, num = com.split()
        deq.append(num)
    
    elif com == "pop":
        print(deq.popleft() if deq else -1)
    
    elif com == "size":
        print(len(deq))

    elif com == "empty":
        print(0 if deq else 1)
    
    elif com == "front":
        print(deq[0] if deq else -1)
    
    elif com == "back":
        print(deq[-1] if deq else -1)