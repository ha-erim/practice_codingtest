import sys
from collections import deque

com = int(sys.stdin.readline().strip())
net = int(sys.stdin.readline().strip())

graph = [[] for _ in range(com + 1)]

for _ in range(net):
    com1, com2 = map(int, sys.stdin.readline().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

visited = [False] * (com + 1)

# print(graph)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(visited.count(True) - 1)
