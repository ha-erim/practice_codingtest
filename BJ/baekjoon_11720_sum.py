import sys
count = sys.stdin.readline().strip()
number = list(sys.stdin.readline().strip())
number = list(map(int,number))
s = sum(number)
print(s)