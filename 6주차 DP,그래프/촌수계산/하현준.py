"""
촌수계산 https://www.acmicpc.net/problem/2644
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(60000)


def dfs_stack(start, pdist):
    global dist
    if start == b:
        dist = pdist
        return pdist

    for node in data[start]:
        if graph[node][start] == 0:
            graph[node][start] = 1
            graph[start][node] = 1
            dfs_stack(node, pdist + 1)

    return pdist


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
data = [[] for _ in range(n + 1)]
dist = -1
for _ in range(m):
    c, d = map(int, input().split())
    data[c].append(d)
    data[d].append(c)

dfs_stack(a, 0)
print(dist)
