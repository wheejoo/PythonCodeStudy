n,m = map(int, input().split())
visited = [0 for i in range(n+1)]

Map = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    Map[a].append(b)
    Map[b].append(a)

def DFS(start):
    s = [start]
    while s:
        t = s.pop()
        visited[t] = 1#방문표시
        near = Map[t]
        for i in near:
            if visited[i] == 1:
                continue
            s.append(i)
    return True

count =  0
for i in range(1,n+1):
    if visited[i]==0:
        DFS(i)
        count+=1
print(count)
#이거 왜 python3 시간초과 나지