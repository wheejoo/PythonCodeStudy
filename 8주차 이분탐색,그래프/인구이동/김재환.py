"""
재귀로 바꿔도 시간초과 남.
이거 python으로 어떻게 제출하여야 하는가....
"""
import sys
from collections import deque

input = sys.stdin.readline
N,L,R = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))

dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]
total = 0
contry = 0
flag=0
def BFS(q, visited):
    global contry
    global total
    global flag

    ori_q = q
    q = deque(q)

    if len(q)==0:
        return

    for _ in range(len(q)):
        y,x = q.popleft()
        contry += 1
        total += Map[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0<= ny < N) and (0<= nx < N) and visited[ny][nx]==0:
                if (L<=abs(Map[y][x] - Map[ny][nx])<=R):
                    q.append([ny,nx])
                    flag = 1
                    visited[ny][nx] = 1
    BFS(q, visited)
    for i in range(len(ori_q)):
        y,x = ori_q[i]
        Map[y][x] = total//contry

count = 0
while True:
    flag = 0
    visited = [[0 for i in range(N)] for i in range(N)] 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:# 안들렀으면 돌기
                print("y,x" , i,j)
                total = 0
                contry = 0
                visited[i][j] = 1
                BFS([[i,j]], visited)
                print(Map)
                total = 0
                contry = 0
    if flag != 0:
        count += 1
    else:
        break
print(count)


"""
DFS로 방문해서 방문한 만큼 되돌려가며 값을 삽입한다.
이후 visited로 방문하지 않은 곳을 탐색한다.
pyp3
"""
"""
import sys
input = sys.stdin.readline
N,L,R = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))
from time import sleep
from collections import deque

dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]

flag = 0
def BFS(y,x, union,visited):
    visited[y][x] = 1
    q = deque([[y,x]])

    while q:
        for _ in range(len(q)):
            y,x = q.popleft()
            union.append([y,x])
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0<= ny < N) and (0<= nx < N) and visited[ny][nx]==0:
                    if (L<=abs(Map[y][x] - Map[ny][nx])<=R):
                        q.append([ny,nx])
                        visited[ny][nx] = 1
def div(total_u):
    for _ in range(len(total_u)):
        u = total_u[_]
        union_sum = 0
        count = len(u)
        for i in range(count):
            y,x = u[i]
            union_sum += Map[y][x]
        for i in range(count):
            y,x = u[i]
            Map[y][x] = union_sum//count

count = 0
union = []
total_u = []
while True:
    flag = 0
    visited = [[0 for i in range(N)] for i in range(N)] 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i,j, union, visited)
                if len(union) > 1: # 연합생성된 경우
                    total_u.append(union)
                    flag = 1
                    union = []
                else: #생성이 되지 않았으면 기존꺼 제외
                    union = []
    div(total_u)
    total_u=[]
    if flag == 0 :
        break
    count+=1
print(count)
"""