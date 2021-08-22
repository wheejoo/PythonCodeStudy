# https://www.acmicpc.net/problem/1707
# 참고
# 이분그래프 - 인접한 정점끼리 다른 색
# 어렵,,

from collections import deque
k = int(input())

def bfs(x):
    visited[x] = 1 #1로 배정
    q = deque()
    q.append(x)
    while q:
        nv = q.popleft()
        for i in graph[nv]:
            if visited[i] == 0: #방문하지X
                visited[i] = -visited[nv] #1이 아닌 다른 flag로 변환
                q.append(i)
            elif visited[i] == visited[nv]: #같으면
                return False #안되니까 False
    return True


for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
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
    