# 다시풀어보기
# 그냥 dfs로 풀면 시간초과 dfs + dp로 풀어야함
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] < graph[x][y]: # 현재 위치(x,y) 기준으로 이동한 곳이(nx,ny) 더 작아야 현재위치에서 이동 위치로 이동가능하다 (내리막길)
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)] # -1로 선언한 이유는 dp안에 값이 0인 경우는 갈 수 있는 경로가 없다는 뜻이다.
# dp[x][y]에 이동할수 있는 경로수 저장
print(dfs(0,0))
