# x를 시작으로 가장 먼곳 간다음 그 곳에서 다시 가장 먼곳으로 풀려했는데
# 왕복 거리가 다르므로 이렇게 풀면 안됨

# 모든 정점에서 x까지 최단거리 구하고
# 다시 x에서 모든 거리까지 최단거리 구해서 서로 더한다음
# 가장 큰 값구함

import heapq
import sys

input = sys.stdin.readline
n, m, x = map(int,input().split())
INF = sys.maxsize
grpah = [[] for _ in range(n+1)]
maxx = 0 

for i in range(m):
    a,b,c = map(int, input().split())
    grpah[a].append((c,b))


def dijstra(index):
    queue = []
    distance[index] = 0
    heapq.heappush(queue, (0, index))
    while queue:
        wei, now = heapq.heappop(queue)
        if distance[now] < wei:
            continue
        for w, next in grpah[now]:
            next_wei = w + wei
            if next_wei < distance[next]:
                distance[next] = next_wei
                heapq.heappush(queue, (next_wei, next))

result = []
for i in range(1, n+1):
    distance = [INF for _ in range(n+1)]
    dijstra(i)
    result.append(distance[x])


distance = [INF for _ in range(n+1)]
dijstra(x)

for i in range(len(result)):
    maxx = max(maxx, result[i] + distance[i+1])

print(maxx)

