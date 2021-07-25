"""
정수 삼각형 https://programmers.co.kr/learn/courses/30/lessons/43105
"""


def solution(triangle):
    dx = [-1, -1]
    dy = [-1, 0]
    n = len(triangle[-1])
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp[-1] = triangle[-1]

    for x in reversed(range(1, n)):
        for y in range(n):
            for i in range(2):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < n and 0 <= yy < len(triangle[xx]):
                    dp[xx][yy] = max(dp[xx][yy], dp[x][y] + triangle[xx][yy])

    return dp[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(solution([[1]]))
