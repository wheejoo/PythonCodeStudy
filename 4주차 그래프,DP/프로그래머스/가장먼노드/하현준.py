"""
가장 먼 노드 https://programmers.co.kr/learn/courses/30/lessons/49189
"""
from collections import deque


def solution(n, edge):
    distance = [int(1e9) for _ in range(n + 1)]
    path = [[] for _ in range(n + 1)]
    for a, b in edge:
        path[a].append(b)
        path[b].append(a)

    q = deque([[1, 0]])
    distance[1] = 0
    while q:
        now, dist = q.popleft()

        for node in path[now]:
            if distance[node] > dist + 1:
                distance[node] = dist + 1
                q.append([node, dist + 1])
    distance = distance[1:]
    print(distance)
    return distance.count(max(distance))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
