"""
벽 부수고 이동하기 https://www.acmicpc.net/problem/2206
메모리 초과
참고 : https://kscodebase.tistory.com/66
"""
from collections import deque
import sys

input = sys.stdin.readline


def dprint(data):
    for a in range(n):
        for b in range(m):
            if data[a][b] == -1:
                print("*", end=" ")
            elif data[a][b] == -2:
                print("■", end=" ")
            else:
                print(data[a][b], end=" ")
        print()
    print("-" * 30)


def bfs():
    global result
    q = deque([[0, 0, 0, 1, [(0, 0)]]])

    while q:
        a, b, count, dist, path = q.popleft()
        if result <= dist:
            continue

        if [a, b] == [n - 1, m - 1]:
            result = min(result, dist)
            print(a, b, dist, "count=", count, "\n", path, len(path))
            dprint(graph)
            dprint(dvisited)
            print("=" * 30)
            continue

        dvisited[a][b] = dist
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if (xx, yy) not in path:
                    if graph[xx][yy] == 0:
                        q.append([xx, yy, count, dist + 1, path + [(xx, yy)]])
                    elif graph[xx][yy] == 1:
                        if count == 0:
                            q.append([xx, yy, count + 1, dist + 1, path + [(xx, yy)]])


result = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dvisited = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]
bfs()

if result == int(1e9):
    print(-1)
else:
    print(result)
