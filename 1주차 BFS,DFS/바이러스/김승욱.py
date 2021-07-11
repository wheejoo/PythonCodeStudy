n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]

distance = [-1 for _ in range(n+1)]

for i in range(t):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = []
queue.append(1)
distance[1] = 0
answer = 0
while queue:
    cur = queue.pop(0)
    for next in graph[cur]:
        if distance[next] == -1:
            answer += 1
            distance[next] = distance[cur] + 1
            queue.append(next)
print(answer)
