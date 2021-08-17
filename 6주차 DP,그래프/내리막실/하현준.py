"""
내리막 길 https://www.acmicpc.net/problem/1520
ㄷㅂㄷㅂㄷㅂ
"""
import sys

sys.setrecursionlimit(60000)
input = sys.stdin.readline

def dfs(x, y):
    global graph, count

    if [x, y] == [m - 1, n - 1]:
        count += 1
        return 1

    if dp[x][y] != -1:
        count += dp[x][y]  # [x][y] 위치에서 [m-1][n-1] 까지 가는 경로의 개수만큼 더해준다.
        return dp[x][y]

    # 여기서 dp값을 0으로 설정
    dp[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n:
            if graph[x][y] > graph[xx][yy]:
                dp[x][y] += dfs(xx, yy)  # [x][y] 위치에서 [m-1][n-1] 까지 가는 경로의 개수를 dp에 저장

    return dp[x][y]


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
# 0이 아닌 -1로 초기화해야 한다. dp 결과값이 0인 경우인지, 초기상태인지 구분할 수 없는 경우 시간초과 발생
dp = [[-1 for _ in range(n)] for _ in range(m)]
count = 0

dfs(0, 0)
print(count)
