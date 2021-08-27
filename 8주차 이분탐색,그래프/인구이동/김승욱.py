# python3 시간초과
# pypy로 제출
# 풀이참고

import collections
import sys

input = sys.stdin.readline
n, l, r = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

queue = collections.deque()

def bfs(a,b,sum):
    flag = False
    queue.append((a,b))
    result = [(a,b)]
    visited[a][b] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                        sum += graph[nx][ny]
                        result.append((nx,ny))
                        queue.append((nx,ny))
                        flag = True
                        visited[nx][ny] = True

    cur = sum // len(result)
    for x,y in result:
        graph[x][y] = cur

    return flag

time = 0
while True:
    chk = False
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                check = bfs(i,j,graph[i][j])
                if check: # 한번이라도 인구이동 했으면 한번 더 돌아야함
                    chk = True

    if not chk:
        break
    time += 1
print(time)
            
