"""
인구 이동 https://www.acmicpc.net/problem/16234
python3 : 시간 초과
pypy3: 1908ms
"""
from collections import deque


def check(a, b):
    return l <= abs(data[a[0]][a[1]] - data[b[0]][b[1]]) <= r


def bfs(px, py, pvisited):
    q = deque([[px, py]])
    pvisited.add((px, py))
    country = set()
    while q:
        i, j = q.popleft()
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if (xx, yy) not in pvisited:
                    if check([i, j], [xx, yy]):  # 인접 국가와 check
                        pvisited.add((xx, yy))
                        country.add((xx, yy))  # 연합에 추가
                        q.append([xx, yy])

    if country:
        country.add((px, py))
        people = sum([data[c[0]][c[1]] for c in country]) // len(country)
        for c in country:  # 인구 이동
            data[c[0]][c[1]] = people
        return True
    # 연합이 만들어지지 않으면 거짓 반환
    return False


n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0

while 1:
    visited = set()
    mcheck = False
    for x in range(n):
        for y in range(n):
            if (x, y) not in visited:  # 방문한적 없는 경우
                if bfs(x, y, visited):
                    mcheck = True
    if mcheck:
        count += 1
    else:
        print(count)
        break
