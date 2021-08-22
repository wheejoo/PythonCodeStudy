# https://www.acmicpc.net/problem/1916
# 참고 - 다익스트라 알고리즘
# 참고 - https://jjangsungwon.tistory.com/28
# 너무 어렵,,

import heapq

INF = int(1e9)
n = int(input()) #도시 수
m = int(input()) #버스 수
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a에서 b로 가는 비용이 c

start, end = map(int,input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start)) #시작 노드로 가기 위한 최단 경로는 0으로 설정
    distance[start] = 0
    while q: #q가 비어있지 X
        dist, now = heapq.heappop(q) #가장 최단 거리가 짧은 노드의 정보 꺼내기
        if distance[now] < dist: #현재 노드가 이미 처리된 노드라면
            continue #bye
        for i in graph[now]: #현재 노드와 연결된 인접한 노드들 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end] #이 부분 다른 코드에서 참고

print(dijkstra(start, end))
