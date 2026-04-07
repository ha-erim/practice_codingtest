import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[0] * m for _ in range(n)]

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] += 1

    while queue:
        (x, y) = queue.popleft()
        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < n
                and 0 <= new_y < m
                and graph[new_x][new_y] != 0
                and visited[new_x][new_y] == 0
            ):
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))


bfs(0, 0)

print(visited[n - 1][m - 1])
