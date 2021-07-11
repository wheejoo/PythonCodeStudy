from collections import deque
from sys import stdin

n, m = map(int, input().split())

matrix = [list(map(int,input())) for _ in range(n)]
#matrix = [stdin.readline().rstrip() for _ in range(n)]


distance = [[-1]*m for _ in range(n)]


# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque([(0,0)])

distance[0][0] = 1
while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(distance[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if(distance[nx][ny] == -1 and matrix[nx][ny] == 1):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
