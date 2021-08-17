"""
아기 상어 https://www.acmicpc.net/problem/16236
"""
from collections import deque

def bfs():
    global time, shark
    sx, sy, ssize = shark

    to_eat = []
    q = deque([[sx, sy, 0]])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = 1

    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if visited[xx][yy] == -1:
                    visited[xx][yy] = 1
                    if graph[xx][yy] <= ssize:
                        q.append([xx, yy, dist + 1])
                        if 1 <= graph[xx][yy] <= 6 and graph[xx][yy] < ssize:
                            to_eat.append([dist + 1, xx, yy, graph[xx][yy]])

    if not to_eat:
        return False

    edist, ex, ey, egraph = sorted(to_eat)[0]

    shark = [ex, ey, ssize]
    fishes.remove([ex, ey, egraph])
    graph[ex][ey] = 0
    time += edist
    return True

n = int(input())
time = 0
count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = []
fishes = []
shark = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark = [i, j, 2]
            graph[i][j] = 0
        elif graph[i][j] != 0:
            fishes.append([i, j, graph[i][j]])

while True:
    # 먹을 수 있는 물고기 중 가까운 놈을 찾는다
    if not bfs():
        print(time)
        break

    count += 1
    if count == shark[2]:
        shark[2] += 1
        count = 0
