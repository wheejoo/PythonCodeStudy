import collections

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    check = [[False]*w for _ in range(h)]
    count = 0

    def bfs(x,y):
        
        queue = collections.deque()
        queue.append((x,y))
        dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 1 and check[nx][ny] == False:
                        check[nx][ny] = True
                        queue.append((nx,ny))
    
    for x in range(h):
        for y in range(w):
            if check[x][y] == False and graph[x][y] == 1:
                bfs(x,y)
                count += 1
    print(count)