INF = int(1e9)
import heapq


def dijkstra(start, end):
    visited = [INF] * (length + 1)
    visited[start] = 0

    pq = [[0, start]]
    heapq.heapify(pq)

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > visited[node]:
            continue

        for i in graph[node]:
            new_node, new_cost = i[0], i[1]
            new_cost += cost

            if new_cost < visited[new_node]:
                visited[new_node] = new_cost
                heapq.heappush(pq, [new_cost, new_node])

    return visited[end]


def solution(n, s, a, b, fares):
    global graph, length
    answer = INF
    length = n

    graph = [[] for _ in range(n + 1)]

    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return answer