"""
파티 https://www.acmicpc.net/problem/1238
pypy3 : 1120ms
python3 : 1496ms
"""
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [float('inf') for _ in range(n + 1)]
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue
        for ndata in graph[now]:
            node, ncost = ndata
            if cost + ncost < dist[node]:
                dist[node] = cost + ncost
                heapq.heappush(q, (dist[node], node))
    return dist


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = 0
for _ in range(m):
    mstart, mend, mtime = map(int, input().split())
    graph[mstart].append([mend, mtime])

xdata = dijkstra(x)
for student in range(1, n + 1):
    if student != x:
        sdata = dijkstra(student)
        result = max(result, xdata[student] + sdata[x])
print(result)
