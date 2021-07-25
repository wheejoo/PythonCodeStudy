import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(n-1):
    x,y,k = map(int, input().split())
    graph[x].append((k,y))
    graph[y].append((k,x))

def dfs(cur):
    
    visited[cur] = True
    for w, next in graph[cur]:
        if visited[next] == False:
            distance[next] = distance[cur] + w
            dfs(next)

# 트리의 지름은 루트노드에서 가장 가중치가 큰 노드에서 다시 가장 가중치가 큰 노드 까지에 거리이다.
dfs(1)

maxDis = distance.index(max(distance))
distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dfs(maxDis)

print(max(distance))

# 1. 트리에서 임의의 정점 x를 잡는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
# 트리의 지름은 정점 y와 정점 z를 연결하는 경로다.




