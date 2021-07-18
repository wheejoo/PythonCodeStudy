# python 시간초과
# pypy로 제출

import collections
n, m = map(int, input().split())

graph = collections.defaultdict(list)
answer = 0
distance = [-1 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(index):
    queue = collections.deque([])
    queue.append(index)
    distance[index] = 0
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if distance[next] == -1:
                distance[next] = distance[cur] + 1
                queue.append(next)

for i in range(1, n+1):
    if distance[i] == -1:
        bfs(i)
        answer += 1

print(answer)
