import collections

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, k):
    queue = collections.deque()
    queue.append((x,y))
    count = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        check[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > k and check[nx][ny] == False:
                    queue.append((nx,ny))
                    check[nx][ny] = True
                    count += 1
    return count

curMax = 0
for i in range(n):
    for j in range(n):
        curMax = max(curMax, graph[i][j])


lenCurMax = 0
for k in range(curMax+1):
    check = [[False] * n for _ in range(n)]
    result = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] > k and check[x][y] == False:
                result.append(bfs(x,y,k))
    
    lenCurMax = max(lenCurMax, len(result))
print(lenCurMax)