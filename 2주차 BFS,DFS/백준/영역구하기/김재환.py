m,n,k = map(int, input().split())

Map = [[0 for i in range(n)] for i in range(m)]

for _ in range(k):
    a,b,c,d = map(int, input().split())
    start = [(m-1-b),(0+a)]
    end = [(m-d),(c-1)]
    for i in range(end[0],start[0]+1):
        for j in range(start[1],end[1]+1):
            Map[i][j] = 1
def DFS(x,y):
    s = [[x,y]]
    Map[x][y] = 1
    dx = [0,0,1,-1] #동서남북
    dy = [1,-1,0,0]
    count = 0
    while s:
        count+=1
        x,y = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<m) and (0<=ny<n) and (Map[nx][ny] == 0):
                s.append([nx,ny])
                Map[nx][ny] = 1
    return count
count=[]
for i in range(m):
    for j in range(n):
        if Map[i][j] == 0:
            count.append(DFS(i,j))
print(len(count))
count.sort()
for i in count:
    print(i, end=' ')