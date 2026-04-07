"""
GPT가 만든 더 짧은 코드 버전

import sys

n = int(sys.stdin.readline())
line = sorted(map(int, sys.stdin.readline().split()))

print(sum(line[i] * (n - i) for i in range(n)))

"""

import sys

n = int(sys.stdin.readline().strip())

line = list(map(int, sys.stdin.readline().split()))

line.sort()

for i in range(n):
    line[i] = line[i] * (n - i)

time = 0
for i in range(n):
    time += line[i]

print(time)
