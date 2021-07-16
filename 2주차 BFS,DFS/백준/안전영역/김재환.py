n = int(input())
Map = []
Max = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    Map.append(tmp)
    if Max < max(tmp):
        Max = max(tmp)
def DFS(start, visited):
    s = [start]
    dx = [0,0,-1,1] # 동서남북
    dy = [1,-1,0,0]

    while s:
        x,y = s.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if (0<=nx<n) and (0<=ny<n) and visited[nx][ny] == 0:
                s.append([nx,ny])

def rain(high, Map):
    visited = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if Map[i][j] <= high:
                visited[i][j] = 1
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                DFS([i,j], visited)
                count+=1
    return count

total = []
for high in range(Max, -1, -1):
    total.append(rain(high, Map))
print(max(total))