# 다익스트라 문제

import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

start, end = map(int, input().split())

queue = []

def dijkstra(start):
    heapq.heappush(queue, (0, start))
    while queue:
        wei, now = heapq.heappop(queue)
        if distance[now] < wei:
            continue
        for w, next in graph[now]:
            next_wei = w + wei
            if distance[next] > next_wei:
                distance[next] = next_wei
                heapq.heappush(queue, (next_wei, next))
dijkstra(start)
print(distance[end])
