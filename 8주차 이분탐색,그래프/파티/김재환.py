"""
다시 생각을 해본다. 
물론 N -> X -> N이다.
원래 다익스트라는 outdegree기준으로 구함.
만약 indegree 기준으로 구한다면? N->X의 값을 구할 수 있다.
그럼 다익스트라 2번하면 N->X->N을 구할수 있다.
"""
import sys
input = sys.stdin.readline
N,M,X = map(int, input().split())

INF = 1000000000
i_adj = [ []for i in range(N+1) ]
o_adj = [ []for i in range(N+1) ]
for _ in range(M):
    a,b,c = map(int, input().split())
    i_adj[b].append((a,c))
    o_adj[a].append((b,c))

import heapq
def daik(pq, adj):
    dp = [INF for i in range(N+1)]
    dp[X] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if dp[node] < cost:
            continue
        for i in range(len(adj[node])):
            end, endcost = adj[node][i]
            if dp[end] > endcost + cost:
                dp[end] = endcost+cost
                heapq.heappush(pq, (dp[end],end))
    return dp
N_X = daik([(0,X)], i_adj)
X_N = daik([(0,X)], o_adj)

big = 0
for i in range(1, N+1):
    big = max(N_X[i] + X_N[i],big)
print(big)





"""
N -> X -> N을 구해야함.
X를 거치고 다시 돌아오는 경우를 여러개 구해야함.
따라서 플로이드가 적합
N=1000 이므로 N^3 = 1,000,000,000 = 10억, 21억 넘지 않아서 ㄱㅊ
이후 경로를 다시 잡아오기

@@@시간초과남

import sys
input = sys.stdin.readline
N,M,X = map(int, input().split())

INF = 1000000000
dp = [[ INF for i in range(N+1)] for i in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    dp[a][b] = c

for i in range(N+1):
    dp[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
memo = []
for i in range(1, N+1):
    memo.append(dp[i][X] + dp[X][i])
print(max(memo))
"""