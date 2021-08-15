# 스패닝트리를 구하는 프림알고리즘은 다익스트라와 유사

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False] * (V+1)
graph = [[] for _ in range(V+1)]

for i in range(E):
    x,y,w = map(int, input().split())
    graph[x].append((w,y))
    graph[y].append((w,x))

def Prim(start): # 인접한 정점들 중에서 최소간선을 선택하며 트리를 확장하는 방법
    heap = []
    heapq.heappush(heap, (0, start))
    answer = 0
    # cnt = 0  cnt를 추가하면 시간단축이 됨
    while heap:
        # if cnt == V: # 트리이기 때문에 n-1개의 간선이 생성되면 완성
        #     return answer
        wei, now = heapq.heappop(heap) # heapq으로 인해 인접한 노드중 가중치가 가장 작은값 선택
        
        if visited[now] == False: # 방문하지 않은곳중에 가중치가 가장 작은값을 선택
            visited[now] = True
            answer += wei
            # cnt += 1
            for w,next in graph[now]: # 현재 이어진 노드와 가중치를 전부 heapq에 넣고 다시 while문 반복
                heapq.heappush(heap, (w, next))
    return answer
print(Prim(1))
