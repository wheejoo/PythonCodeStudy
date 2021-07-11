from collections import deque
k = int(input())

def bfs(x):
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        nv = q.popleft()
        for i in graph[nv]:
            if visited[i] == 0:
                visited[i] = -visited[nv]
                q.append(i)
            elif visited[i] == visited[nv]:
                return False
    return True


for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    check = True
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if visited[i] == 0:
            if not bfs(i):
                check = False
                break
    print('YES' if check else 'NO')
