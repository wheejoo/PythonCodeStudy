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
            visited[i] = start #부모노드가 없으면 start로 설정
            dfs(i,graph,visited)
dfs(1,graph,visited)

for i in range(2,n+1):
    print(visited[i])

##시간초과.....
# import sys
# sys.setrecursionlimit(10000)
#
# n = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# for i in range(n-1):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def dfs(v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             graph.append(i)
#             dfs(i)
# dfs(1)
# for i in range(2,n+1):
#     print(graph[i][0])
