"""
트리의 부모 찾기 https://www.acmicpc.net/problem/11725
"""
from collections import deque
import sys

# 10 ** 6 : 메모리 초과, 50000 : recursionError
sys.setrecursionlimit(60000)
input = sys.stdin.readline


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


# 스택 344ms
def dfs_stack(start):
    stack = deque([start])
    visited[start] = 1
    while stack:
        now = stack.pop()
        for node in path[now]:
            if visited[node] == 0:
                root[node] = now
                visited[node] = 1
                stack.append(node)


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
