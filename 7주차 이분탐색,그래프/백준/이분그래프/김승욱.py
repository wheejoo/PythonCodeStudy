# 서로 인접한 정점이 같은 색(값)이면 이분그래프가 아니다.

import collections
import sys

t = int(input())
input = sys.stdin.readline
for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    for j in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    queue = collections.deque()
    
    def bfs(start):
        queue.append(start)
        check[start] = 1
        while queue:
            cur = queue.popleft()
            for next in graph[cur]:
                if check[next] == 0:
                    check[next] = check[cur] * -1
                    queue.append(next)
                elif check[next] == check[cur]:
                    return False
        return True

    for j in range(1, n+1):
        if check[j] == 0:
            chk = bfs(j)
            if chk == False:
                break
    if chk:
        print("YES")
    else:
        print("NO")