"""
욕심쟁이 판다 https://www.acmicpc.net/problem/1937
시간초과 -> visited 변수가 필요 없었네..
"""
from collections import deque
import sys


# 시간초과 (뭐가 잘못되었는지 잘 모르겠음..)
def dfs(a, b):
    global dp

    result = 0
    q = deque({(a, b, 0)})
    while q:
        x, y, count = q.pop()
        if dp[x][y] != -1:
            result = max(result, dp[x][y] + count)
            continue
        check = True
        for c in range(4):
            xx = x + dx[c]
            yy = y + dy[c]
            if 0 <= xx < n and 0 <= yy < n:
                if forest[xx][yy] > forest[x][y]:
                    check = False
                    q.append((xx, yy, count + 1))

        if check:
            result = max(result, count)

    dp[a][b] = result


# 해설보고 품
def dfs2(a, b):
    global dp, answer

    if dp[a][b] != -1:
        return dp[a][b]

    dp[a][b] = 1
    temp = 0
    for k in range(4):
        xx = a + dx[k]
        yy = b + dy[k]
        if 0 <= xx < n and 0 <= yy < n:
            if forest[xx][yy] > forest[a][b]:
                temp = max(temp, dfs2(xx, yy))

    dp[a][b] += temp
    answer = max(answer, dp[a][b])

    return dp[a][b]


sys.setrecursionlimit(40000)
# 만약 dx,dy가 바뀌면 RecursionError 뜸
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(sys.stdin.readline().rstrip())
dp = [[-1 for _ in range(n)] for _ in range(n)]
forest = []
answer = 0
for _ in range(n):
    forest.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        dfs2(i, j)

print(answer)
