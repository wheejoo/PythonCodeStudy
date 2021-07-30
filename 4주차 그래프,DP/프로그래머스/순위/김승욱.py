# 플로이드 와샬 풀이 답지봄
from collections import Counter

def solution(n, results):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 알수 없을경우 0
    for x,y in results: # 이겼을경우 1, 졌을경우 -1
        graph[x][y] = 1
        graph[y][x] = -1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1

    ans = 0
    print(graph)
    for i in range(1,n+1):
        print(Counter(graph[i])) # graph[i] 원소에 대한 숫자를 세어준다.
        print(Counter(graph[i])[0]) # graph[i]에 0에 갯수를 세어준다.
        if Counter(graph[i])[0] == 2: # 인덱스 n+1로 만들어서 인덱스0이랑, 자기자신을 포함해 0이 2개만 있으면 i는 순위를 알 수 있다.
            ans += 1
    return ans

# bfs 풀이 실패

# import collections
# def solution(n, results):
#     answer = 0
#     graph = [[] for _ in range(n+1)]
#     distance = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
#     queue = collections.deque()
    
#     for result in results:
#         graph[result[0]].append(result[1])
#         #graph[result[1]].append(result[0])
        
#     def bfs(index):
#         visited = [False for _ in range(n+1)]
#         queue.append(index)
#         while queue:
#             cur = queue.popleft()
#             visited[cur] = True
#             for next in graph[cur]:
#                 if visited[next] == False:
#                     distance[index][next] =1
#                     visited[next] = True
#                     queue.append(next)
        
#     for i in range(1,n+1):
#         bfs(i)
#     print(distance)
#     for i in range(1,len(distance)-1):
#         for j in range(1, len(distance)):
#             distance[i+1][j] += distance[i][j]
#     cnt = 0
#     distance[n].sort(reverse=True)
#     print(distance[n])
    
#     if distance[n][0] != 0:
#         answer += 1
    
#     for i in range(1,n):
#         if distance[n].count(distance[n][i]) == 1:
#             if distance[n][i-1] - distance[n][i] == 1:
#                 answer += 1
#         else:
#             break
#     return answer