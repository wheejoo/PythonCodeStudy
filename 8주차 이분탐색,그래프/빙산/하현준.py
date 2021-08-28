"""
빙산 https://www.acmicpc.net/problem/2573
pypy3 : 928ms
python3 : 시간초과 파이썬 너 ~ 진짜 느림보구나!
"""
from collections import deque
import sys

input = sys.stdin.readline


def melting(mices):
    dices = []
    mdata = []
    for ice in mices:
        x, y = ice
        zero = 0
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 0:
                    zero += 1
        if graph[x][y] - zero > 0:
            mdata.append([x, y, graph[x][y] - zero])
            dices.append([x, y])
        else:
            mdata.append([x, y, 0])
    return mdata, dices


def count_bing(cices):
    tcount = 0
    visited = set()
    for ice in cices:
        a, b = ice
        if (a, b) in visited:
            continue

        q = deque([[a, b]])
        visited.add((a, b))
        tcount += 1

        if tcount > 1:
            return True

        while q:
            x, y = q.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < n and 0 <= yy < m:
                    if (xx, yy) not in visited and graph[xx][yy] != 0:
                        visited.add((xx, yy))
                        q.append([xx, yy])
    return False


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = []
ices = []
year = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] != 0:
            ices.append([i, j])

while 1:
    # 빙하 녹기
    data, ices = melting(ices)

    # 빙산이 다 녹을 때까지 분리되지 않을 때
    if not ices:
        print(0)
        break

    for d in data:
        r, s, melt = d
        graph[r][s] = melt

    year += 1

    # 덩어리 세기
    if count_bing(ices):
        print(year)
        # 빙산이 분리될 경우 break
        break
