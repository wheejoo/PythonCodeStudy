from collections import deque

def solution(n, edge):
    # 초기화
    M = [[] for i in range(n+1)]
    for i in range(len(edge)):
        a,b = edge[i]
        M[a].append(b)
        M[b].append(a)
    
    # 1번 노드가 루트
    q = deque([1])
    visited = [0 for i in range(n+1)]
    visited[1] = 1
    
    #BFS
    number = 0
    while q:
        number = len(q)
        for _ in range(len(q)):
            node = q.popleft()
            childlist = M[node]
            for child in childlist:
                if(visited[child] == 0):
                    q.append(child)
                    visited[child] = 1    
    return number