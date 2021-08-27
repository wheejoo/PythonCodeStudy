# 위상정렬 문제
# dp 생각못함

import collections
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    answer = 0
    graph = [[] for _ in range(N+1)]
    value = [0]+list(map(int,input().split()))
    distance = [0 for _ in range(N+1)]
    dp = [0] * (N+1)
    for i in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        distance[y] += 1

    end = int(input())

    queue = collections.deque()

    for i in range(1, N+1):
        if distance[i] == 0:
            queue.append(i)
            dp[i] = value[i]

    def bfs():
        global answer
        while queue:
            cur = queue.popleft()
            for next in graph[cur]:
                dp[next] = max(dp[next], dp[cur] + value[next])
                distance[next] -= 1
                if distance[next] == 0:
                    queue.append(next)
            
    bfs()
    print(dp)
    print(dp[end])