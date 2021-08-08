# 플로이드 와샬 문제

import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x,y,w = map(int, input().split())
    graph[x][y] = min(graph[x][y], w) # 입력값 보면 같은 경로 다른 가중치를 입력하는 경우가 있음

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
