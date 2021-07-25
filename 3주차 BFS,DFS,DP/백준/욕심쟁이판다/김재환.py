### 판다 쉑 너무 어렵다
### DP랑 어떻게 연결되는건지 모르겠다
### 이해한대로는 DP가 비어있을때 DFS실행해서 각 dp마다 경로를 설정해준다.
### 그럼 DP를 사용가능한데 그 이유는 이미 구한 애들과 비교해서 
### 상화좌우에서 자기보다 큰 좌표가 존재하면 그 좌표의 값을 가져오면 되서이다.

import sys
input = sys.stdin.readline

from sys import setrecursionlimit 
setrecursionlimit(10**9)

n = int(input())
M = []
for i in range(n):
    tmp = list(map(int, input().split()))
    M.append(tmp)
dp = [[0 for i in range(n)] for i in range(n)]

dy = [0, 0, 1, -1]  # 동서남북
dx = [1, -1, 0, 0]  # 동서남북
def DFS(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if (0 <=ny<n) and (0<=nx<n) and M[ny][nx] > M[y][x]:
            dp[y][x] = max(dp[y][x], DFS(ny,nx)+1)
    return dp[y][x]

tmp = 0
for i in range(n):
    for j in range(n):
        tmp = max(tmp, DFS(i,j))
print(tmp)

"""
### 시간초과남 각 좌표마다 최댓값을 알아내어 DFS가 필요할때만 돌림
n = int(input())
M=[]
oM =[]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        oM.append([tmp[j],i,j])
    M.append(tmp)
oM.sort()

def DFS(i,j):
    s = [[i,j,1]]
    dy = [0,0,1,-1] #동서남북
    dx = [1,-1,0,0] #동서남북
    big = 0
    while s:
        y,x,z = s.pop()
        if z > big:
            big = z
        for i in range(4):
            ny  = y+dy[i]
            nx  = x+dx[i]
            if (0<=ny<n) and (0<=nx<n) and M[ny][nx] > M[y][x]:
                s.append([ny,nx,z+1])
        print(s)
    return big

def main():
    big = 0
    for t in oM:
        v,i,j = t
        print(v,i,j)
        if big > n*n-v-1:#시작부터 나올수 있는 최댓값
            return big
        tmp = DFS(i,j)
        if tmp > big:
            big = tmp
    return big
print(main())
"""
