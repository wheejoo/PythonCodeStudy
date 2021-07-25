"""
트리의 부모 찾기 https://www.acmicpc.net/problem/11725
"""
from collections import deque
import sys

# 10 ** 6 : 메모리 초과, 50000 : recursionError
sys.setrecursionlimit(60000)


# 재귀 584ms
def dfs(start):
    if visited[start] == 1:
        return

    visited[start] = 1
    for node in path[start]:
        if visited[node] == 0:
            dfs(node)
            root[node] = start
    return start


# 스택 시간초과
def dfs_stack(start):
    stack = deque([[start, visited]])

    while stack:
        now, nvisit = stack.pop()
        if nvisit[now] != 0:
            continue
        nvisit[now] = 1
        for node in path[now]:
            if nvisit[node] == 0:
                root[node] = now
                stack.append([node, nvisit + [node]])


n = int(input())
path = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
root = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)
dfs(1)
# dfs_stack(1)
for r in root[2:]:
    print(r)
