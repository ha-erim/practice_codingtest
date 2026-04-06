"""
-----------
인접 행렬 버전
-----------

import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())

# 리스트 컴프리헨션 문법 유의
matrix = [[False] * (node + 1) for _ in range(node + 1)]

for _ in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    matrix[node1][node2] = matrix[node2][node1] = True

visited_dfs = [False] * (node + 1)
visited_bfs = visited_dfs.copy()


def dfs(V):
    visited_dfs[V] = True
    print(V, end=" ")
    for i in range(1, node + 1):
        if matrix[V][i] == True and visited_dfs[i] == False:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, node + 1):
            if visited_bfs[i] == False and matrix[v][i] == True:
                queue.append(i)
                visited_bfs[i] = True


dfs(start)
print()
bfs(start)

"""

"""
-------------
재귀없는 dfs
-------------

def dfs(start):
    visited = [False] * (node + 1)
    stack = [start]

    while stack:
        v = stack.pop()
        if visited[v]:
            continue

        visited[v] = True
        print(v, end=" ")

        # 재귀 DFS 순서 맞추려면 역순으로 넣기
        for nxt in reversed(graph[v]):
            if not visited[nxt]:
                stack.append(nxt)
                
"""
import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for g in graph:
    g.sort()

# print(graph)

visited = [False] * (node + 1)


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(start)
print()
visited = [False] * (node + 1)
bfs(start)
