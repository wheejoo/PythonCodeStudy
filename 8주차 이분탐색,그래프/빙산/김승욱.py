# python3 시간초과
# pypy로 제출

import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


dx,dy = [-1,1,0,0], [0,0,-1,1]

queue = collections.deque()

def bfs(i,j):
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    value[x][y] += 1
                elif graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    
                    queue.append((nx,ny))
time = 0
flag = False
while True:
    visited = [[False]*m for _ in range(n)]
    value = [[0]*m for _ in range(n)]
    check = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                bfs(i,j)
                check += 1
    if check == 0:
        flag = False
        break
    if check >= 2:
        flag = True
        break
    for x in range(n):
        for y in range(m):
            graph[x][y] = graph[x][y] - value[x][y]
            if graph[x][y] < 0:
                graph[x][y] = 0
    time += 1

if flag:
    print(time)
else:
    print(0)