"""
합승 택시 요금 https://programmers.co.kr/learn/courses/30/lessons/72413
"""
import heapq

INF = float('inf')


def dijkstra_atob(n, start, a, b, graph):
    q = []
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue
        for i in graph[now]:
            ncost, node = i
            ndist = cost + ncost
            if dist[node] > ndist:
                dist[node] = ndist
                heapq.heappush(q, (ndist, node))

    return dist[a], dist[b]


def solution(n, s, a, b, fares):
    result = []
    graph = [[] for _ in range(n + 1)]
    path = [[] for _ in range(n + 1)]
    for fare in fares:
        x, y, d = fare
        graph[x].append([d, y])
        graph[y].append([d, x])

    q = []
    dist = [INF for _ in range(n + 1)]
    dist[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue

        for i in graph[now]:
            ncost, node = i
            ndist = cost + ncost
            if dist[node] > ndist:
                dist[node] = ndist
                path[node] = [node, now]
                heapq.heappush(q, (ndist, node))

    for i in range(1, n + 1):
        da, db = dijkstra_atob(n, i, a, b, graph)
        result.append(dist[i] + da + db)

    return min(result)


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
