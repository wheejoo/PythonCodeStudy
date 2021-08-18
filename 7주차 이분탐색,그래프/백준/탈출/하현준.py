"""
탈출 https://www.acmicpc.net/problem/3055
"""
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
gosm = deque([])
water = deque([])
graph = []
for i in range(r):
    graph.append(list(input()))
    for j in range(c):
        if graph[i][j] == "S":
            gosm.append([i, j, 0])
        elif graph[i][j] == "*":
            water.append([i, j])

while True:
    wtemp = []  # 물이 찰 위치
    while water:
        wx, wy = water.popleft()
        for k in range(4):
            xx = wx + dx[k]
            yy = wy + dy[k]
            if 0 <= xx < r and 0 <= yy < c:
                if graph[xx][yy] != "*" and graph[xx][yy] != "X" and graph[xx][yy] != "D":
                    graph[xx][yy] = "*"
                    wtemp.append([xx, yy])

    water = deque(wtemp[:])

    temp = []
    while gosm:
        a, b, dist = gosm.popleft()
        # 고슴도치 이동 시작
        for k in range(4):
            xx = a + dx[k]
            yy = b + dy[k]
            if 0 <= xx < r and 0 <= yy < c:
                if graph[xx][yy] != "S" and graph[xx][yy] != "*" and graph[xx][yy] != "X":
                    if graph[xx][yy] == "D":
                        print(dist + 1)
                        exit(0)
                    graph[xx][yy] = "S"
                    temp.append([xx, yy, dist + 1])
    if not temp:
        print("KAKTUS")
        exit(0)

    gosm = deque(temp[:])