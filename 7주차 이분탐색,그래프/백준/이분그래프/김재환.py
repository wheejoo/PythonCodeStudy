'''
DFS로 돌면서 1그룹과 2그룹으로 생각하고
미리 그룹이 정해진경우 자신과 다르면 ㄱㅊ
자신과 그룹이 같으면 ㅇㄱㅊ
'''
import sys
input = sys.stdin.readline # 요게 필순
def DFS(start, adj, visited):
    stack = [start]
    visited[start] = 1
    while stack:
        node = stack.pop()
        adjnode = adj[node]
        for adjn in adjnode:
            if visited[adjn] == -1: #들르지 않은경우
                visited[adjn] = visited[node]^1
                stack.append(adjn)
            else: # 이미 들른경우
                if visited[adjn] == visited[node]:# 같은 집합인경우 실패
                    return 0
    return 1

T = int(input())
for _ in range(T):
    V,E = map(int, input().split())
    adj = [[] for i in range(V+1)]
    for i in range(E):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [-1 for i in range(V+1)]
    flag = 1
    for i in range(1,V+1):
        if visited[i] == -1:
            flag = DFS(i, adj, visited)
            if flag == 0:
                break
    if flag == 1:
        print("YES")
    else:
        print("NO")