"""
처음 빙산은 1덩어리
1. 빙산 파악하기 (DFS로 filter 구하기)
2. 빙산 filter로 줄이기
3. 덩어리 파악하기
pypy3 가 한계.... 이유 찾아보기
"""
import sys
input = sys.stdin.readline

N,M = map(int, input().split()) # 행, 열
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))
dy = [-1,1,0,0] #상하좌우
dx = [0,0,-1,1]
   
def DFS(i,j, visited, Map2):
    s = [(i,j)]
    while s:
        y,x = s.pop()
        if visited[y][x] == 1:
            continue
        visited[y][x] = 1
        calc = 0
        for i in range(4):
            ny = y  + dy[i]
            nx = x  + dx[i]
            if (0<=ny<N) and (0<=nx<M):
                if Map[ny][nx] <= 0:
                    calc += 1
                else:
                    s.append((ny,nx))
        Map2[y][x] = Map[y][x] - calc

def find(visited,Map2):
    land = 0
    for i in range(1,N):
        for j in range(1,M):
            if visited[i][j] == 0 and Map[i][j] > 0:
                DFS(i,j,visited, Map2)
                land += 1
                if land > 1:
                    return land
    return land
# 빙산 줄일꺼 찾고 덩어리 찾기
count = 0
while True:
    visited = [[0 for i in range(M)] for i in range(N)]
    Map2=[[0 for i in range(M)] for i in range(N)]
    land = find(visited, Map2)

    if land == 0:
        count = 0
        break
    if land > 1:#덩이리여러개면 연산중지
        break
    count+=1
    Map = Map2
print(count)

