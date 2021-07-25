# https://www.acmicpc.net/problem/1967
##답은 45,, 채점은 틀렸습니다,,

import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, value = map(int,input().split())
    graph[parent].append((child, value))
    graph[child].append((parent, value))

def dfs(start, graph, value):
    if start == 1:
        value[start] = 0 #시작1 가중치0
    for node, v in graph[start]:
        if value[node] == 0: #현재 가중치 0이면
            value[node] = value[start] + v #현재 가중치 + 다음노드 가중치
            dfs(node, graph, value)

ans1 = [0 for _ in range(n+1)]
dfs(1,graph,ans1) #시작점1 - 가장 먼 노드 탐색

max_node = ans1.index(max(ans1)) #가장 먼 노드
ans2 = [0 for _ in range(n+1)]
dfs(max_node,graph,ans2) #가장 먼 노드로 길이 구하기

print(max(ans2))


