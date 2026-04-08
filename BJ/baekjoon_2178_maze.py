import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))

# print(maze)

# n, m = 7, 7
# maze = [
#     [1, 0, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1],
# ]

visited = [[False] * (m) for _ in range(n)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(x, y):
    queue = deque([(x, y)])
    # count = 0
    # print(queue)
    while queue:
        v_x, v_y = queue.popleft()
        # print(v_x, v_y)
        if visited[v_x][v_y] == False:
            visited[v_x][v_y] = True
            for dx, dy in dir:
                new_x, new_y = v_x + dx, v_y + dy
                if (
                    0 <= new_x < n
                    and 0 <= new_y < m
                    and maze[new_x][new_y] != 0
                    and visited[new_x][new_y] == False
                ):
                    queue.append([new_x, new_y])
                    maze[new_x][new_y] = maze[v_x][v_y] + 1


search(0, 0)
print(maze[-1][-1])
