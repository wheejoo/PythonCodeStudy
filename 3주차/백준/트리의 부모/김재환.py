from collections import deque
n = int(input())
M = [ [] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    M[a].append(b)
    M[b].append(a)

q = deque([1])
visited = [0 for i in range(n+1)]
parentlist = [0 for i in range(n+1)]
#BFS하기~
while q:
    p = q.popleft()
    visited[p] = 1
    linklist = M[p]
    for child in linklist:
        if visited[child] == 0:
            parentlist[child] = p
            q.append(child)
    print(q)
for i in range(2, len(parentlist)):
    print(parentlist[i])