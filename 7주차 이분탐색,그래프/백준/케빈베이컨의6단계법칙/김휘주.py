# https://www.acmicpc.net/problem/1389
# 참고 - 플로이드 워셜 알고리즘

INF = int(1e9)
n,m = map(int,input().split())
friend = [[INF] * (n+1) for _ in range(n+1)] #친구 그래프 초기화

#친구 관계 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    friend[a][b] = 1
    friend[b][a] = 1

#자기 자신에서 자기 자신으로 가는 거리 0
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            friend[a][b] = 0
            
#플로이드 워셜
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            friend[a][b] = min(friend[a][b], friend[a][k] + friend[k][b])

#이 부분 다른 코드 참고,, - https://claude-u.tistory.com/337
result = []
for i in friend:
    # print(i)
    result.append(sum(i))
    # print(result)
    # print(min(result))
print(result.index(min(result)))






# 트리 부모 찾기랑,, 비슷,,??
# 답은 나오는데 틀렸습니다,,,
#
# import sys
# sys.setrecursionlimit(10**9)
#
# n,m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# visited = [[] for _ in range(n+1)]
#
# for _ in range(n):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def dfs(start, graph, visited):
#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] = start
#             dfs(i,graph,visited)
#
# dfs(1,graph,visited)
# result = []
# for i in range(2,n+1):
#     result.append(visited[i])
#
# print(result[0])