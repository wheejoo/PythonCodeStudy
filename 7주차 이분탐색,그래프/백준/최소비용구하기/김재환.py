'''
모든 쌍 최단거리인줄 알고, 플로이드 워샬로 구하려고 했는데
시간제한이 0.5라서 단일 시작점알고리즘이란걸 알게됨.
단일 시작점은 다익스트라와 벨만-포드가 존재함.
음수 가중치 없으니 다익으로 ㄱㄱㅆ
다익스트라-> pq사용
'''
import heapq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = 2100000000
adj = [[] for i in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    adj[a].append([b,c])

start,final = map(int, input().split())

# 메모이제이션 배열 선언
dp = [INF for i in range(N+1)]
dp[start] = 0
# 우선순위큐 선언
pq = []
heapq.heappush(pq, [0,start])

while pq:
    cost,mid = heapq.heappop(pq)
    if dp[mid] < cost:
        continue
    for end, endcost in adj[mid]:
        if dp[end] > cost+endcost:
            dp[end] = cost+endcost
            heapq.heappush(pq, [dp[end],end])
print(dp[final])