"""
ACM Craft https://www.acmicpc.net/problem/1005
pypy3 : 1656ms
python3: 1596ms
"""
from collections import deque
import sys

input = sys.stdin.readline  # 이거 안하면 시간 초과


def topoloy_sort(pindegree, pgraph, pdata, odata, pw):
    q = deque([])
    for i in range(1, len(pindegree)):
        if pindegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for node in pgraph[now]:
            pindegree[node] -= 1
            odata[node] = max(odata[now] + pdata[node], odata[node])
            if pindegree[node] == 0:
                q.append(node)

    print(odata[pw])


for _ in range(int(input())):
    n, k = map(int, input().split())
    data = [-1] + list(map(int, input().split()))
    indegree = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    topoloy_sort(indegree, graph, data, data[:], w)
