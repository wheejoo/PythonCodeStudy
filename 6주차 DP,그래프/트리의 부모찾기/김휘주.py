# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, graph, visited):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            dfs(i,graph,visited)

dfs(1,graph,visited)
for i in range(2,n+1):
    print(visited[i])
