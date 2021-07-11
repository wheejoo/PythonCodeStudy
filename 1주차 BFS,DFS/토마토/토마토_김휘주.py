from collections import deque
#m 가로칸 수, n세로칸 수
m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
q = deque([])

def bfs():
    answer = 0
    while q:
        answer += 1
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny < m:
                    if graph[nx][ny] == 0:
                        q.append((nx,ny))
                        graph[nx][ny] = graph[x][y] + 1

    #토마토 모두 익지X
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                return -1
    return answer-1

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            q.append((i,j))

print(bfs())
