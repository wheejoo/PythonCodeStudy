import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
for i in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
            parents[next] = cur
            dfs(next)
dfs(1)
for i in range(2, n+1):
    print(parents[i])