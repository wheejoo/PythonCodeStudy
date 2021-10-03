"""
1. 비어있는 칸 구하기
2. 비어있는 값을 기준으로 조합구하기(permutation아님)
3. 조합만큼 루프 돌기
4. 조합 걸고 2위치에서 DFS를 통해 넓이 구하기
5. 0의 넓이 구하기
6. 계속 비교
"""
from itertools import combinations
import copy
from time import sleep
N, M = map(int, input().split())  # 세로 가로
Map = []
loc2 = []
loc1 = []
loc0 = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):  # 2의 위치, 0의 위치 구하기
        if tmp[j] == 2:
            loc2.append([i, j])
        elif tmp[j] == 0:
            loc0.append([i, j])
        else:
            loc1.append([i, j])
    Map.append(tmp)
# 조합구하기
com1 = list(combinations(loc0, 3))

big = 0
# 조합으로 루프 돌리기
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for com in com1:
    tmp = copy.deepcopy(Map)
    # 벽세우기
    for _ in range(3):
        tmp[com[_][0]][com[_][1]] = 1
    # 2기준 DFS 실행하며 넓이 계산
    s = list(loc2)
    count = 0
    while s:
        y, x = s.pop()
        count += 1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and tmp[ny][nx] == 0:  # 인덱스 가능
                tmp[ny][nx] = 2
                s.append([ny, nx])
    # 0의 넓이 구하기
    print(tmp)
    print(count)
    area = N*M - count - (len(loc1) + 3)
    if big < area:
        big = area
    print(area)
print(big)
