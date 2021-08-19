'''
BFS에서 물의 이동과, 고슴도치 이동
q에서는 물이라면 물을 체크, 고슴도치라면 고슴도치 체크

'''
R,C = map(int, input().split())
D,S = 0,0
Map = []

from collections import deque
q = deque([])

for r in range(R):
    tmp = list(input())
    for c in range(C):
        if tmp[c] == 'S':
            S = ['S', r, c]
        if tmp[c] == 'D':
            D = [r,c]
    Map.append(tmp)
# 물 구하기
for r in range(R):
    for c in range(C):
        if Map[r][c] == '*':
            q.append(["*",r,c])
q.append(S)

def BFS(q):
    dy = [-1,1,0,0] # 상하좌우
    dx = [0,0,-1,1]
    time = 0
    while q:
        time += 1
        for _ in range(len(q)):
            t = q.popleft()
            char, y,x = t
            if [y,x] == D:
                return time-1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0<=ny<R) and (0<=nx<C) :# 가능 인덱스
                    if char == '*': # 물일때
                        if Map[ny][nx] == '.' or Map[ny][nx] == 'S':# 비어있거나 고슴도치이면 먹어버린다.
                            Map[ny][nx] = char
                            q.append([char, ny, nx])
                    elif char == 'S': # 고슴도치일때
                        if Map[ny][nx] == '.' or Map[ny][nx] == 'D': # 물`이 아니거나 도착지이면
                            Map[ny][nx] = char
                            q.append([char, ny, nx])
    return -1
tmp = BFS(q) 
if tmp == -1:
    print("KAKTUS")
else:
    print(tmp)