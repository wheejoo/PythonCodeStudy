import collections
t = int(input())


for i in range(t):
    n = int(input())
    x, y = map(int, input().split())
    rx , ry = map(int, input().split())
    dx, dy = [-1,-2, -1, -2, 1, 2, 1, 2], [2, 1, -2, -1, 2, 1, -2, -1]
    distance = [[0] * n for _ in range(n)]
    queue = collections.deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if x == rx and y == ry:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
    print(distance[rx][ry])
                