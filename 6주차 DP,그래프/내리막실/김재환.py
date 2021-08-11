
M,N = map(int, input().split()) # 세로 가로
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
visited = [[-1 for i in range(N)] for i in range(M)]
visited[M-1][N-1] = 1
# DFS
dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]

def DFS(start):
    y,x = start
    if visited[y][x] != -1: #온적 있으면
        return visited[y][x] # 해당 경우의 수를 그대로 넘겨준다.
    tmp = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<=ny<M) and (0<=nx<N):# 인덱스 적정범위
            if graph[ny][nx] < graph[y][x]:
                tmp += DFS([ny,nx])
    visited[y][x] = tmp # 분기한 경우에, 각 갈래의 경우의 수를 더해준다.
    return visited[y][x] # 갱신된 자신의 경우의 수를 넘겨준다.

DFS([0,0])
print(visited[0][0])
"""
import sys
sys.setrecursionlimit(250000) # 500 * 500

M,N = map(int, input().split()) # 세로 가로
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

# DFS
dy = [-1,1,0,0] #상하좌우
dx = [0,0,-1,1]

count =  0
def DFS(start):
    global count
    y,x = start
    if [y,x] == [M-1, N-1]:
        count += 1
        return 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<=ny<M) and (0<=nx<N):# 인덱스 적정범위
            if graph[ny][nx] < graph[y][x]:
                DFS([ny,nx])

DFS([0,0])
print(count)
"""