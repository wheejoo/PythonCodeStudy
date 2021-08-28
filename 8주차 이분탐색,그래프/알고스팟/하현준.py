"""
알고스팟 https://www.acmicpc.net/problem/1261
pypy3 : 208ms
Python3 : 332ms
"""
from collections import deque


def dprint(data):
    for dd in data:
        for d in dd:
            print(d, end=" ")
        print()
    print("-" * 40)


m, n = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
crash = [[float('inf') for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

crash[0][0] = 0
q = deque([[0, 0, 0]])

while q:
    x, y, crash_cnt = q.popleft()
    print(q)
    print("!", x, y, crash_cnt)
    dprint(crash)
    if crash_cnt > crash[x][y]:
        continue
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < m:
            if data[xx][yy] == 1 and crash_cnt + 1 < crash[xx][yy]: # 이게 keypoint
                crash[xx][yy] = crash_cnt + 1
                q.append([xx, yy, crash[xx][yy]])
            if data[xx][yy] == 0 and crash_cnt < crash[xx][yy]:
                crash[xx][yy] = crash_cnt
                q.append([xx, yy, crash[xx][yy]])

print(crash[n - 1][m - 1])
