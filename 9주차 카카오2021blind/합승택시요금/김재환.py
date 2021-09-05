
import heapq
INF = 30000000

def daik(start,definition):
    pq = [[0,start]]
    
    dp = [INF for i in range(N+1)]
    dp[start] = 0
    while pq:
        cost,node = heapq.heappop(pq)
        if dp[node] < cost:
            continue
        for i in range(len(adj[node])): # 인접리스트
            end, endcost = adj[node][i]
            if dp[end] > cost + endcost:
                dp[end] = cost+endcost
                heapq.heappush(pq, [dp[end],end])
    return dp[definition]
def solution(n, s, a, b, fares):
    # n=node, s = start 
    # 같이 가는경우 갈라질 지점을 정한다.
    # 갈라지는 지점부터 A와 B의 도착지점의 최솟값을 구한다.
    # 플로이드로 구하고 n^3 + n, 다익스트라 nlogn mid((S->mid) + (mid->A) + (mid->B)) 
    # 다익스트라가 더 빨라서 당첨
    
    # fares에 대한 전처리
    global N
    N = n
    global adj 
    adj = [ [] for i in range(N+1) ]
    for i in fares:
        start,end,cost = i
        adj[start].append((end,cost))
        adj[end].append((start,cost))
    
    small = INF
    for mid in range(1,n+1):
        totalcost = daik(s,mid) + daik(mid,a) + daik(mid,b)
        if totalcost < small:
            small = totalcost
    
    return small