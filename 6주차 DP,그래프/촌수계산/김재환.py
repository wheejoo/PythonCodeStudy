n = int(input())
x,y = map(int, input().split())
m = int(input())
adj = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0 for i in range(n+1)]

def DFS(s):
    while s:
        node,c = s.pop()
        if node == y:
            return c
            
        visited[node] = 1

        childs = adj[node]
        for child in childs:
            if visited[child] == 0 :
                s.append([child,c+1])
    return -1

s = [[x,0]]
print(DFS(s))