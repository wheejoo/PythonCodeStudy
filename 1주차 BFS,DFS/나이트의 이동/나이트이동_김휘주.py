from collections import deque
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(x1,y1,x2,y2):
    q = deque()
    q.append((x1,y1))
    while q:
        x,y = q.popleft()
        if x == x2 and y == y2:
            print(graph[x2][y2])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0<= ny < l:
                if graph[nx][ny] == 0: #끝좌표가 0이라면
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y]+1

n = int(input())
for _ in range(n):
    l = int(input())
    x1, y1 = map(int,input().split()) #시작
    x2, y2 = map(int,input().split()) #끝
    graph = [[0] * l for _ in range(l)]
    bfs(x1,y1,x2,y2)