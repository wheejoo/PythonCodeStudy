"""
트리의 지름 https://www.acmicpc.net/problem/1167
모르겠음
"""
import sys

sys.setrecursionlimit(60000)
input = sys.stdin.readline


def dic_enu(data):
    return dict(enumerate(data))


def dfs(start, value):
    global edges, visited, data

    if data[start]:
        return max(data[start], value)

    visited[start] = 1
    ret = [0, 0]
    for e in edges[start]:
        node, cost = e
        if visited[node] == 0:
            visited[node] = 1
            data[node] = cost + value
            dfs(node, data[node])
            if ret[1] < data[node]:
                ret = node, data[node]

    return ret


v = int(input())

edges = [[] for _ in range(v + 1)]
answer = -1
for _ in range(v):
    temp = list(map(int, input().split()))[:-1]
    for i in range(len(temp[1:]) // 2):
        b, c = temp[1:][i * 2:i * 2 + 2]
        edges[temp[0]].append([b, c])

visited = [0] * (v + 1)
data = [0] * (v + 1)
idx, _ = dfs(1, 0)
idx, val = dfs(idx, 0)
print(val)

"""
6
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 6 7 -1
6 5 7 -1
"""
