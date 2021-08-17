'''
빨강,파랑 같이 움직임, 기울이기는 둘다 안움직일때까지

완전 탐색 해야함 , 최소 횟수로 빠져나와야함. -> BFS

1. 이동방향 정하기
2. 이동시키기 
3. 만약 이동중에 구멍에 볼 들어가면 함수 반환

세부적으로 어떤 공을 먼저 움직이게 할지
상하좌우 방향에 따라 먼저 움직여야 하는 공이 다르다.
1. 상 : y 좌표가 작은거 부터 이동
2. 하 : y 좌표가 큰거 부터 이동
3. 좌 : x 좌표가 작은거 부터 이동
4. 우 : x 좌표가 큰거 부터 이동

=> visited 없으니 통과....?
'''

N,M = map(int, input().split()) # 세로 가로
Map = []
R, B = 0,0
for i in range(N):
    tmp = list(input())
    Map.append(tmp)
    for j in range(M):
        if tmp[j] == "R":
            R = [i,j]
        if tmp[j] == "B":
            B = [i,j]

dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]

from collections import deque
from time import sleep
def go(direction,R,B):
    b1, b2 = R,B
    reverse = 0
    print("go:",direction, R,B, reverse)
    if direction == [-1,0]:#상
        if R[0] < B[0]:#y가 작으면 그대로
            b1, b2 = R,B
        else:
            b1, b2 = B,R
            reverse = 1
    elif direction == [1,0]:#하
        if R[0] < B[0]:# y가 작으면 반대로
            b1,b2 = B,R
            reverse = 1
        else:
            b1,b2 = R,B
    elif direction == [0,-1]:#좌
        if R[1] < B[1]: # x가 작으면 그대로
            b1,b2 = R,B
        else:
            b1,b2 = B,R
            reverse = 1
    else:#우
        if R[1] < B[1]: # x가 작으면 반대로
            b1,b2 = B,R
            reverse = 1
        else:
            b1,b2 = R,B
    # 본격적으로 값을 밀어본다.
    outdoor1 = False
    outdoor2 = False
    y,x = b1
    while True: # b1을 먼저 움직인다.
        ny = y + direction[0]
        nx = x + direction[1]
        if (0<ny<N-1) and (0<nx<M-1): # 허용 인덱스 범위
            if Map[ny][nx] == "O": # 출구 만남
                y = ny
                x = nx
                outdoor1 = True
                break
            elif Map[ny][nx] != '#': #벽이 아니라면 움직이기 가능
                y = ny
                x = nx
                continue
            else:
                break
        else:
            break
    y2,x2 = b2
    while True: # b2를 움직인다.
        ny2 = y2 + direction[0]
        nx2 = x2 + direction[1]
        if (0<ny2<N-1) and (0<nx2<M-1): # 허용 인덱스 범위
            if Map[ny2][nx2] == "O":
                y2 = ny2
                x2 = nx2
                outdoor2 = True
                break
            elif Map[ny2][nx2] != '#' and [ny2,nx2]!=[y,x]: #벽이 아니거나 앞의 공이 아니면 움직이기 가능
                y2 = ny2
                x2 = nx2
                continue
            else: #갈수 없는경우
                break
        else:
            break
    # 정산시작~ #outdoor가 0이면
    print(y,x,y2,x2)
    print(outdoor1, outdoor2)
    if reverse == 0: # R , B
        if outdoor1==False and outdoor2==False: # 다른방향도 해야함.
            q.append([[y,x],[y2,x2]])
            return 0
        elif outdoor1==True and outdoor2==False:# 성공!
            return 1
    else: # B, R
        if outdoor1==False and outdoor2==False: # 다른방향도 해야함.
            q.append([[y2,x2],[y,x]])
            return 0
        elif outdoor1==False and outdoor2==True:# 성공!
            return 1

def BFS():
    time = 0
    while time < 10:
        time += 1
        for _ in range(len(q)):
            r,b = q.popleft()
            y,x = r
            y2,x2 = b
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                ny2 = y2 + dy[i]
                nx2 = x2 + dx[i]
                # 둘중에 하나라도 움직이는게 가능하면됨
                if ((0<ny<N-1) and (0<nx<M-1)) or ((0<ny2<N-1) and (0<nx2<M-1)):# 인덱스 이동가능
                    if Map[ny][nx] != '#' or Map[ny2][nx2] != '#': # 이동가능
                        if go([dy[i],dx[i]], r,b) == 1: # 어디로 이동할건지, 이동시작하는 r,b좌표보내준다.
                            return time
        print(q)
    return -1
q = deque([[R,B]])
print(BFS())
