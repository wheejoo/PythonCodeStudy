import collections

n = int(input())
a, b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = collections.deque()

def bfs(index):
    queue.append(index)
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                distance[next] = distance[cur] + 1
                queue.append(next)

bfs(a)
if distance[b] == 0:
    print(-1)
else:
    print(distance[b])

