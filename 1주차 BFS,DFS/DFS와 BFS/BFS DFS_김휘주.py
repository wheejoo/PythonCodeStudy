import sys
sys.setrecursionlimit(10000) #런타임 에러 방지
from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and (graph[v][i] == 1):
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = False
    while q:
        nv = q.popleft()
        print(nv, end=' ')
        for i in range(1, n + 1):
            if visited[i] and (graph[nv][i] == 1):
                q.append(i)
                visited[i] = False

print(dfs(v))
print(bfs(v))
#출력 값 끝에 None 질문,,
