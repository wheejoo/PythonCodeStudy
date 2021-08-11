import sys
input = sys.stdin.readline

n = int(input())
adj = [ [] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [ 0 for i in range(n+1)]
visited = [0 for i in range(n+1)]

s = [1]
while s:
    node = s.pop()
    visited[node] = 1

    childs = adj[node]
    for child in childs:
        if visited[child] == 0: # 비어있음
            parent[child] = node
            s.append(child)
    
for i in range(2, n+1):
    print(parent[i])