def DFS(w,h,Map , start):
    s = [start]
    dx = [0,0,1,-1,-1,-1,1,1] #동서남북 왼위 오위 왼아래 오아래
    dy = [1,-1,0,0,-1,1,-1,1]

    while s:
        x,y = s.pop()
        Map[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<h) and (0<=ny<w) and (Map[nx][ny]==1):
                s.append([nx,ny])     

while True:
    w,h = 0,0
    a = input()
    w,h = map(int, a.split())
    if [w,h] == [0,0]:
        break
    Map = []
    for i in range(h):
        Map.append(list(map(int, input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                DFS(w,h,Map, [i,j])
                count+=1
    print(count)