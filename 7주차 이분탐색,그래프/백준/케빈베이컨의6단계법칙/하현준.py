"""
케빈 베이컨의 6단계 법칙 https://www.acmicpc.net/problem/1389
"""
from collections import deque


def bfs(start):
    distance = [-1 for _ in range(n + 1)]
    q = deque([[start, 0]])
    distance[start] = 0

    while q:
        now, dist = q.popleft()
        for node in friend[now]:
            if distance[node] == -1 or distance[node] > dist + 1:
                distance[node] = dist + 1
                q.append([node, distance[node]])
    return sum(distance[1:])


n, m = map(int, input().split())
result = []
friend = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(1, n + 1):
    result.append([bfs(i), i])

result.sort()
print(result[0][1])
