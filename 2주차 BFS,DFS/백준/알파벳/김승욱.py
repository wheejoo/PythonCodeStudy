### bfs ###

import collections
import sys

r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]

queue = set([(0,0,graph[0][0])])


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs():
    result = 1
    while queue:
        x,y,visitied = queue.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] not in visitied:
                    next_visitied = visitied + graph[nx][ny]
                    queue.add((nx,ny,next_visitied))
                    result = max(result, len(next_visitied))
    return result
print(bfs())

### dfs ###

import sys

input = sys.stdin.readline
r,c = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]

alpha = [0] * 26

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if alpha[arr[nx][ny]] == 0:
                alpha[arr[nx][ny]] = 1
                dfs(nx, ny, count+1)
                alpha[arr[nx][ny]] = 0

ans = 1
alpha[arr[0][0]] = 1
dfs(0,0,1)
print(ans)