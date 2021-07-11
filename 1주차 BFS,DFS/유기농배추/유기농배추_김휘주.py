from collections import deque
t = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1: #배추심은곳
                    q.append((nx,ny))
                    graph[nx][ny] = -1

for _ in range(t):
    m, n, k = map(int, input().split())
    #땅
    graph = [[0] * m for _ in range(n)]
    #배추
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1 ###why???
    #지렁이
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: #배추0
                bfs(i,j)
                cnt += 1 #지렁이 +1
    print(cnt)