"""
트리의 지름 https://www.acmicpc.net/problem/1967
완료
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(60000)


def dfs(start):
    global graph, data, visited_n, visited_e
    if data[start]:
        return max(data[start])

    visited_n[start] = 1
    for node, nvalue in graph[start]:
        if visited_n[node] == 0:
            visited_n[node] = 1
            data[start].append(dfs(node))
            visited_e.append({node})

    if not data[start]:
        data[start] += [0]

    for nod, val in graph[start]:
        if nod not in visited_e:
            return max(data[start]) + val


n = int(input())
if n == 1:
    print(0)
    exit(0)

graph = [[] for _ in range(n + 1)]
visited_n = [0] * (n + 1)
visited_e = []
data = [[] for _ in range(n + 1)]
result = -1
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dfs(1)
for dt in data:
    if len(dt) > 2:
        dt.sort(reverse=True)
        result = max(result, sum(dt[0:2]))
    elif len(dt):
        result = max(result, sum(dt))
print(result)
