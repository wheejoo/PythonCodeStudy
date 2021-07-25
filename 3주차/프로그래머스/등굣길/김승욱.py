import collections

def solution(m, n, puddles):
    answer = 0
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for i in range(len(puddles)):
        graph[puddles[i][1]-1][puddles[i][0]-1] = -1 # puddles 안에도 m,n 순으로 들어있어서 뒤집어서 넣어준다.
    
    queue = collections.deque()
    queue.append((0,0))
    dx, dy = [0, 1], [1, 0]
    graph[0][0] = 1
    def bfs():
        while queue:
            x,y = queue.popleft()
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0 <= ny < m:
                    if graph[nx][ny] != -1 and visited[nx][ny] == False: # 방문하지 않았던 곳이면 경우의 수 늘려주고 queue에 넣어준다.
                        visited[nx][ny] = True
                        graph[nx][ny] += graph[x][y]
                        queue.append((nx,ny))
                    elif graph[nx][ny] != -1:
                        graph[nx][ny] += graph[x][y] # 방문했던 곳이여도 경우의 수는 늘리기 위해 더해준다.
    bfs()
    print(graph)
    return (graph[n-1][m-1]) % 1000000007