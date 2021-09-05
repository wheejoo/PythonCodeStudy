import heapq
import sys
def solution(n, s, a, b, fares):
    answer = 0
    INF = sys.maxsize
    minn = INF
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    for x,y,z in fares:
        graph[x].append((z,y))
        graph[y].append((z,x))
        
    
    def dijstra(s):
        queue = []
        heapq.heappush(queue,(0, s))
        distance[s] = 0
        while queue:
            wei, now = heapq.heappop(queue)
            if distance[now] < wei:
                continue
            for w, next in graph[now]:
                next_wei = wei + w
                if distance[next] > next_wei:
                    distance[next] = next_wei
                    heapq.heappush(queue, (next_wei, next))
    dijstra(s)
    temp_distance = distance
    for i in range(1,n+1):
        distance = [INF for _ in range(n+1)]
        dijstra(i)
        answer = temp_distance[i] + distance[a] + distance[b]
        minn = min(minn, answer)
    return minn