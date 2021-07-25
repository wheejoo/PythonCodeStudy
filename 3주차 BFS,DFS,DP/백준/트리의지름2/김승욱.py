import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())

graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
distance = [0 for _ in range(V+1)]
for i in range(V):
    demo = list(map(int, input().split()))
    cnt = 0
    while True:
        if demo[1+cnt] == -1:
            break
        graph[demo[0]].append((demo[2+cnt],demo[1+cnt]))
        cnt += 2

def dfs(cur):
    visited[cur] = True
    for w, next in graph[cur]:
        if visited[next] == False:
            distance[next] = distance[cur] + w
            dfs(next)
dfs(1)

maxIndex = distance.index(max(distance))
visited = [False for _ in range(V+1)]
distance = [0 for _ in range(V+1)]
dfs(maxIndex)
print(max(distance))
