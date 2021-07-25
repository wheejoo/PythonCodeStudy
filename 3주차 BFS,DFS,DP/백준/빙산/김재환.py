n,m = map(int , input().split())
M = []
big = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    M.append(tmp)

from time import sleep
def DFS(i,j, visited):
    s = [[i,j]]
    visited[i][j] = 1
    dy = [0,0,1,-1] #동서남북
    dx = [1,-1,0,0]
    while s:
        y,x = s.pop()
        visited[y][x]=1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0<=ny<n) and (0<=nx<m) and M[ny][nx] > 0 and visited[ny][nx]==0:
                s.append([ny,nx])

def findIsland():
    count =0
    visited = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if  M[i][j] != 0 and visited[i][j] == 0:
                DFS(i,j,visited)
                count+=1
    if count >= 2:
        return True
    else:
        return False

def melt():
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    fileter = [[0 for i in range(m)] for i in range(n)]

    for y in range(n):
        for x in range(m):
            if M[y][x] != 0:
                for z in range(4):
                    ny = y + dy[z]
                    nx = x + dx[z]
                    if (0<=ny<n) and (0<=nx<m) and M[ny][nx] == 0:
                        fileter[y][x] +=1
    for y in range(n):
        for x in range(m):
            M[y][x] -= fileter[y][x]
            if M[y][x] < 0:
                M[y][x] = 0
def checkice():
    total = 0
    for i in range(n):
        total += sum(M[i])
    if total == 0:
        return True
    else:
        return False

flag = 0
i = 0
while True:
    if findIsland():
        flag = i
        break
    else:
        if checkice():
            break
        melt()
        i+=1

if flag != 0:
    print(flag)
else:
    print(0)
