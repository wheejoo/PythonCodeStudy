# 모든 정점을 연결하는 가장 작은 최소비용을 구해야한다. 
# 모든 정점을 연결하는 최소 연결 횟수는 n-1개 이고 n-1개의 간선으로 연결되어 있으면 트리형태를 가지고있어 스패닝트리 문제이다.
# Prim을 사용하였다.

import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

queue = []
heapq.heappush(queue, (0,1))

def Prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                heapq.heappush(queue, (next_wei, next_node))
    return answer

print(Prim())