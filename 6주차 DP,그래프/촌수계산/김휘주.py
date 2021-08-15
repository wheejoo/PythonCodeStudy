# https://www.acmicpc.net/problem/2644
import sys
sys.setrecursionlimit(10**9)

n = int(input()) #사람수
a,b = map(int,input().split()) #서로 다른 두 사람 번호
m = int(input()) #관계 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split()) #부모 자식 간의 관계
    graph[x].append(y)
    graph[y].append(x)

# visited = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(v, graph, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            dfs(i, graph, visited)

dfs(a, graph, visited) #a - start
print(visited[b] if visited[b] > 0 else -1)