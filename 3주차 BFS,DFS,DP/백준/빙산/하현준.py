"""
빙산 https://www.acmicpc.net/problem/2573
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = []
ices = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] != 0:
            ices.append([i, j])

year = 0
count = 1
while True:
    data = []
    # 빙하 녹기
    for ice in ices:
        x, y = ice
        zero = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 0:
                    zero += 1
        if graph[x][y] - zero > 0:
            data.append([x, y, zero])
        else:
            data.append([x, y, -1])

    ices = []
    for d in data:
        x, y, melt = d
        if melt == -1:
            graph[x][y] = 0
        else:
            graph[x][y] -= melt
            ices.append([x, y])

    # 빙산이 다 녹을 때까지 분리되지 않을 때
    if not ices:
        print(0)
        break

    # 덩어리 세기
    tcount = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for ice in ices:
        a, b = ice
        if visited[a][b] == 1:
            continue
        q = deque([[a, b]])
        visited[a][b] = 1
        tcount += 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < n and 0 <= yy < m:
                    if visited[xx][yy] == 0 and graph[xx][yy] != 0:
                        visited[xx][yy] = 1
                        q.append([xx, yy])
    count = tcount
    year += 1

    # 빙산이 분리될 경우 break
    if count > 1:
        print(year)
        break
