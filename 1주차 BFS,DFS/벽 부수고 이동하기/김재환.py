from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
M = []
for i in range(n):
    tmp = list(map(int, input().rstrip()))
    M.append(tmp)

def BFS():
    dx = [0,0,1,-1] #동 서 남 북
    dy = [1,-1,0,0]
    q = deque([[0,0,0]])
    if n == 1 and m == 1:
        if M[0][0] == 1:
            return -1
        else:
            return 1
    M[0][0] = 2
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            x,y,z = q.popleft()
            if [x,y] == [n-1,m-1]:
                return time+1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0<=nx<n) and (0<=ny<m): #인덱스 허용범위
                    if z == 0: #벽뿌를 안함
                        if M[nx][ny] == 0:
                            M[nx][ny] = 2
                            q.append([nx,ny,z])
                        elif M[nx][ny] == 1:
                            q.append([nx,ny,1])
                            M[nx][ny] = 4
                        elif M[nx][ny] == 3:
                            q.append([nx,ny,z])
                            M[nx][ny]=2
                    else: #벽뿌를 함
                        if M[nx][ny] == 0:
                            M[nx][ny] = 3
                            q.append([nx,ny,z])
    return -1
print(BFS())
