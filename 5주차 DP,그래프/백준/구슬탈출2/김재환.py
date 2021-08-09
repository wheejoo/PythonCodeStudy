# 50퍼에서 처참히 실패

from collections import deque
n,m = map(int, input().split()) #세로가로
# visited 초기화
visitedR = [[0 for i in range(m)] for i in range(n)]
visitedB = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i==0 or j ==0 or i==n-1 or j==m-1:
            visitedR[i][j] = 1
            visitedB[i][j] = 1
Map = []
R =[0,0]
B =[0,0]
for r in range(n):
    tmp = list(input())
    for c in range(len(tmp)):
        if tmp[c] == 'R':
            R = [r,c]
        if tmp[c] == "B":
            B = [r,c]
    Map.append(tmp)

def move(direction, b1, b2, q, order):
    print("실질 움직임",direction, b1, b2, q, order)
    flag = 0
    y,x = b1
    y2,x2 = b2
    # 이동중에 A,B가 O에 도착하는 경우
    while True:
        #빨강공 움직이기
        ny = y + direction[0]
        nx = x + direction[1]
        if (0<ny<n-1) and (0<nx<m-1):
            # 탈출조건
            if Map[ny][nx] == "O":
                y = ny
                x = nx
                flag = 1
                break
            if Map[ny][nx] != '#' and [ny,nx]!=[y2,x2]:#벽이 아니고 파랑공이 아니면 가능
                y = ny
                x = nx
            else:
                break
        else:
            break
    while True:
        # 파랑공 움직이기
        ny2 = y2 + direction[0]
        nx2 = x2 + direction[1]
        if (0<ny2<n-1) and (0<nx2<m-1):
            # 탈출조건
            if Map[ny2][nx2] == "O":
                y2 = ny2
                x2 = nx2
                flag = 2
                break
            if Map[ny2][nx2] != '#' and [ny2,nx2] != [y,x]:#벽이 아니고 빨강공의 위치가 아니어야함.
                y2 = ny2
                x2 = nx2
            else:
                break
        else:
            break
    if flag == 0:
        if order == 1: #빨강이 먼저 움직였음
            q.append([[y,x],[y2,x2]])
            visitedR[y][x] = 1
            visitedB[y2][x2] = 1
        elif order == 2:# 파랑이 먼저 움직였음
            q.append([[y2,x2],[y,x]])
            visitedR[y2][x2] = 1
            visitedB[y][x] = 1
    
    if order == 2: #파랑 먼저
        if flag == 1:# 실패
            flag = 2
        elif flag == 2:#성공
            flag = 1
    return flag # 1:잘 도착, 2:B가 도착, 0:한번더 해야함.

def go_end(direction, R,B,q):# 파랑공이 먼저 움직이는지 빨강공이 먼저 움직이는지 고민해보아야한다. 코드 다시 짜야될한듯
    #동쪽 : x값이 큰거 먼저 이동
    #서쪽 : x값이 작은거 먼저 이동
    #남쪽 : y값이 작은거 먼저 이동
    #북쪽 : y값이 큰거 먼저 이동
    print("goend:",direction, R,B,q)
    flag = 0
    if direction == [0,1]:#동쪽
        if R[1] < B[1]:# x값이 큰거 먼저 이동
            flag = move(direction, B,R,q,2)
        else:
            flag = move(direction, R,B,q,1)
    elif direction == [0,-1]:#서쪽
        if R[1] < B[1]: # x값이 작은거 먼저 이동
            flag = move(direction, R,B,q,1)
        else:
           flag =  move(direction, B,R,q,2)
    elif direction == [1,0]:#남쪽
        if R[0] < B[0]:# y값이 큰거 먼저 이동
            flag = move(direction, B,R,q,2)
        else:
            flag = move(direction, R,B,q,1)
    elif direction == [-1,0]:#북쪽
        if R[0] < B[0]:# y값이 작은거 먼저 이동
            flag = move(direction, R,B,q,1)
        else:
            flag = move(direction, B,R,q,2)
    return flag # 1:잘 도착, 2:B가 도착, 0:한번더 해야함.

def BFS(R,B):
    dy = [0,0,1,-1] #동서남북
    dx = [1,-1,0,0]
        
    q = deque([])
    q.append([R,B])
    visitedR[R[0]][R[1]] = 1
    visitedB[B[0]][B[1]] = 1
    count = 0
    while q:
        count+=1
        print("COUNT:",count)
        if count > 10:
            count = -1
            return count
        for _ in range(len(q)):
            R,B = q.popleft()
            y,x = R
            y2,x2 = B
            print("RRRR:",y,x)
            for i in range(4):#동서남북
                ny = y + dy[i]
                nx = x + dx[i]
                ny2 = y2 + dy[i]
                nx2 = x2 + dx[i]
                if (0<ny<n-1 and 0<nx<m-1) or (0<ny2<n-1 and 0<nx2<m-1): #가능범위
                    # 빨강공이나 파랑공 움직일 조건
                    if Map[ny][nx] != "#" or Map[ny2][nx2] != "#":
                        if visitedR[ny][nx]!=1 or visitedB[ny2][nx2]!=1:
                            flag = go_end([dy[i],dx[i]],R,B,q)
                            if flag == 1:# 잘도착함
                                return count
        print(q)
    return -1
print(BFS(R,B))