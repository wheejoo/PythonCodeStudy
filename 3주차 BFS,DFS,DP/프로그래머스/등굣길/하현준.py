"""
등굣길 https://programmers.co.kr/learn/courses/30/lessons/42898
문제를 잘 읽어라 제발 좀
"""


# 반복문
def solution(m, n, puddles):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[m - 1][n - 1] = 1
    for a in reversed(range(m)):
        for b in reversed(range(n)):
            for i in range(2):
                xx = a - dx[i]
                yy = b - dy[i]
                if 0 <= xx < m and 0 <= yy < n:
                    if [xx + 1, yy + 1] not in puddles:
                        dp[xx][yy] += dp[a][b]

    return dp[0][0] % 1000000007


# 재귀 dfs
def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[n - 1][m - 1] = 1

    def dfs(x, y):
        if dp[x][y] != 0:
            return dp[x][y]

        for i in range(2):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if [yy + 1, xx + 1] not in puddles:
                    dp[x][y] += dfs(xx, yy)
        return dp[x][y]

    dfs(0, 0)
    return dp[0][0] % 1000000007


dx = [1, 0]
dy = [0, 1]
print(solution(4, 3, [[2, 2]]))
