import sys

n, k = map(int, sys.stdin.readline().split())

cash = []
count = 0

for _ in range(n):
    cash.append(int(sys.stdin.readline().strip()))

cash.sort(reverse=True)
# print(cash)


for i in cash:
    if i <= k:
        num = k // i
        k = k % i
        count += num
    if k == 0:
        break

print(count)
# print(f"count : {count}")
# print(f"cash : {k}")
