import sys
from collections import Counter

N = int(sys.stdin.readline())

graph = []

for i in range(1, N + 1):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# N = 5
# graph = [
#     [0, 1, 1, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0],
# ]
# print(graph)

visited = [[0] * N for _ in range(N)]
result = []
dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def search(x, y):
    visited[x][y] = True
    count = 1

    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < N and N > new_y >= 0:
            if graph[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                count += search(new_x, new_y)
    return count


for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and visited[x][y] == 0:
            result.append(search(x, y))


# print(f"graph \n {graph}\n")
# print(f"visited \n {visited}")

# print(f"print result : {result}")
print(len(result))

for r in sorted(result):
    print(r)
