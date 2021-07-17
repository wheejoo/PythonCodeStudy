n = int(input())
NMap = []
WMap = []
for i in range(n):
    tmp = list(input())
    NMap.append(list(tmp))
    for j in range(n):
        if tmp[j] == "G":
            tmp[j] = "R"
    WMap.append(tmp)
def DFS(x,y, Map):
    s = [(x,y,Map[x][y])]
    Map[x][y] = 0
    dx = [0,0,1,-1] #동서남북
    dy = [1,-1,0,0]

    while s:
        x,y,z = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<n) and (0<=ny<n) and (Map[nx][ny] == z):
                s.append([nx,ny,z])
                Map[nx][ny] = 0   

#일반인
count = [0,0]
for i in range(n):
    for j in range(n):
        if NMap[i][j] != 0:
            DFS(i,j, NMap)
            count[0] += 1
        if WMap[i][j] != 0:
            DFS(i,j,WMap)
            count[1] += 1
for i in count:
    print(i, end=" ")