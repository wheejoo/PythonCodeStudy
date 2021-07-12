import sys
sys.setrecursionlimit(10000)#재귀 런타임에러 방지

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def solution():
    cnt = 0
    visited = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i,visited)
            cnt += 1
    return cnt

def dfs(v,visited):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e,visited)

print(solution())