"""
최소비용 구하기 https://www.acmicpc.net/problem/1916
플로이드 워셜 : 시간 초과 O(N^3)
다익스트라 : ok O(E * logV)
"""
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue
        for node, ndist in data[now]:
            if dist[node] > cost + ndist:
                dist[node] = cost + ndist
                heapq.heappush(q, (dist[node], node))


result = 0
INF = float('inf')
n = int(input())
m = int(input())
dist = [INF for _ in range(n + 1)]
temp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    temp[a][b] = min(temp[a][b], c)
    data[a].append([b, temp[a][b]])
start, end = map(int, input().split())

dijkstra(start)
print(dist[end])
