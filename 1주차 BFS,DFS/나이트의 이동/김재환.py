from collections import deque
T = int(input())

def BFS(l, start, end):
    M = [[0 for i in range(l)] for i in range(l)]
    M[start[0]][start[1]] = 1
    q = deque([start])

    dx = [-1,-2,-2,-1,1,2,2,1] # 행
    dy = [-2,-1,1,2,2,1,-1,-2] # 열
    time = -1
    while q:
        time+=1
        for i in range(len(q)):#개수만큼 반복
            x,y =  q.popleft()
            if [x,y] == end:
                return time
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0<=nx<l) and (0<=ny<l) and (M[nx][ny]==0):
                    M[nx][ny] = 1
                    q.append([nx,ny])
    
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(BFS(l, start, end))