import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y,k):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if graph[nx][ny] > k:
                visited[nx][ny] = True
                dfs(nx,ny,k)

ans = 0
for k in range(max(map(max,graph))): #최대값에 따라 달라지니까
    cnt = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if graph[i][j] > k:
                    cnt += 1
                    visited[i][j] = True
                    dfs(i,j,k)
    ans = max(ans, cnt)
print(ans)