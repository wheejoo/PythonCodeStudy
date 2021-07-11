from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def BFS(Map, target, visited):
    visited[target] = 1
    q = deque([target])
    while q:
        target = q.popleft()
        targets = Map[target]
        for t in targets:
            if visited[t] == 0: #방문 x
                visited[t] = -visited[target]
                q.append(t)
            else: #방문 했으면 비교
                if visited[t] == visited[target]:#이분 그래프 아님
                    return "NO"
    return "YES"
for _ in range(T):
    v,e = map(int, input().split())
    Map = [[] for i in range(v+1)]
    visited = [0  for i in range(v+1)]
    for i in range(e):
        a,b=map(int,input().split())
        Map[a].append(b)
        Map[b].append(a)
    flag = True
    for i in range(1,v+1):
        if visited[i] == 0:
            if BFS(Map, i, visited) == "NO":
                flag = False
                break
    if flag == True:
        print("YES")
    else:
        print("NO")
