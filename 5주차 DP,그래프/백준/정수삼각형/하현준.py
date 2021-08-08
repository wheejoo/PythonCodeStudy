"""
정수 삼각형 https://www.acmicpc.net/problem/1932
"""
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(i)] for i in range(1, n + 1)]
dp[n - 1] = graph[n - 1]

for i in reversed(range(n - 1)):
    for j in range(len(dp[i])):
        dp[i][j] = max(graph[i][j] + dp[i + 1][j], graph[i][j] + dp[i + 1][j + 1])

print(dp[0][0])
