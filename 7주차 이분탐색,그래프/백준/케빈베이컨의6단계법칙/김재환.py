'''
N->? 로 가는 경우의 수를 구하면된다.
즉, 모든쌍 최단거리 알고리즘을 사용한다.

N이 100이기 때문에 N^3을 해도 시간초과가 나진 않을것.
'''

INF = 1000
N,M = map(int, input().split())

dp = [[INF for i in range(N+1)] for i in range(N+1)]

adj = [[]for i in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

    dp[a][a] = 0
    dp[b][b] = 0

# 플워는 kij
for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][k]+dp[k][j], dp[i][j])

small = INF
smallF = 1
for i in range(N,0,-1):
    if small >= sum(dp[i][1:]):
        small = sum(dp[i][1:])
        smallF = i
print(smallF)
