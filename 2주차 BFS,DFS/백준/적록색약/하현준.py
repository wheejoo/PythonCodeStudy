"""
적록색약 https://www.acmicpc.net/problem/10026
"""
from collections import deque


def bfs(graph):
    count = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # R=ord('R'), G=ord('G'), B=ord('B'), 방문안한 곳 = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                color = ord(graph[x][y])

                count += 1
                q = deque([[x, y]])
                visited[x][y] = color
                while q:
                    ax, ay = q.popleft()
                    for i in range(4):
                        xx = ax + dx[i]
                        yy = ay + dy[i]

                        if 0 <= xx < n and 0 <= yy < n:
                            if visited[xx][yy] == 0 and ord(graph[xx][yy]) == color:
                                visited[xx][yy] = color
                                q.append([xx, yy])
    return count


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
agraph = []
bgraph = []
for _ in range(n):
    data = list(input())
    agraph.append(data)
    bgraph.append([('G' if c == 'G' or c == 'R' else c) for c in data])

print(bfs(agraph), bfs(bgraph))
