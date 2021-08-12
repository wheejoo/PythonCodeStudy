'''
조건
1. 먹을수 있어야함. -> 먹을수 있는것만 mq에 저장
2. 거리가 가까워야함. -> 주위 돌때마다 확인
3. 위 물고기 선호
4. 왼쪽 물고기 선호
=> BFS 탐색 -> 물고기 전부 찾기 -> 하나면 하나먹으러 가기
-> 여러개면 조건에 따른 우선순위중 첫번째만 먹기
-> 다시 BFS탐색시작

q 에는 상어의 위치, 레벨, 먹을 물고기수, life
mq 에는 물고기의 y좌표,x좌표
visited 필요함. 단 먹이 먹으면 갱신
map은 전역으로 변경해줌

'''
n = int(input())
Map =[]
shark = 0
for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 9:
            shark = [y,x]
    Map.append(tmp)

from collections import deque
from time import sleep
def BFS(sharkinfo):
    dy = [-1,1,0,0] # 상하좌우
    dx = [0,0,-1,1]

    loc, size, ex, life = sharkinfo

    visited = [[0 for i in range(n)] for i in range(n)]
    visited[loc[0]][loc[1]] = 1
    Map[loc[0]][loc[1]] = 0 # 자신이 출발하는 곳은 비어있게 한다.
    
    q = deque([loc])
    mq = deque([])

    time  = 0
    while q:
        time += 1
        for _ in range(len(q)):
            loc = q.popleft()
            y,x = loc
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0<=ny<n) and (0<=nx<n) and visited[ny][nx]==0 and Map[ny][nx] <= size: # 움직일수 있는 조건
                    # 먹을수 있는지
                    if 0< Map[ny][nx] < size: # 먹을수 있는 경우 pq에 저장
                        mq.append([ny,nx])
                    else: # 지나갈 수만 있다면 q에 저장
                        q.append([ny,nx])
                    visited[ny][nx] = 1
        # 한바퀴 돌았기 때문에 여기서 pq에 들어간게 있으면 뽑아서 BFS실행시킨다.
        if len(mq) != 0: # 먹을놈들 발견
            mq = deque(sorted(mq, key=lambda x : (x[0],x[1])))
            my,mx = mq.popleft() # 가장 조건에 부합하는 물고기쉑 뽑기
            # 먹이주기
            if ex == 1: # 렙업시기
                size += 1
                ex = size
            else: # 렙업시기 아님
                ex -= 1
            return BFS([[my,mx], size, ex, life + time])
    
    return life

print(BFS([shark,2,2,0]))


