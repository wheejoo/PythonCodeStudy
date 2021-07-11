N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = []

def dfs(x, y):
    #방문체크
    global cnt
    cnt += 1
    graph[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == '1':
                dfs(nx, ny)
#시작점 확인
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
