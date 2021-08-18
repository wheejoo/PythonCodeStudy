"""
이분 그래프 https://www.acmicpc.net/problem/1707
비연결 그래프인 경우도 고려해야 한다.
"""
from collections import deque

for _ in range(int(input())):
    flag = True
    v, e = map(int, input().split())

    path = [[] for _ in range(v + 1)]
    data = [0 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        path[a].append(b)
        path[b].append(a)

    for i in range(1, v + 1):
        q = deque([i])
        if data[i] == 0:
            data[i] = 1

        while q:
            now = q.popleft()
            for node in path[now]:
                if data[node] == 0:
                    data[node] = data[now] * -1
                    q.append(node)
                elif data[node] == data[now]:
                    flag = False
                    break
    if flag:
        print("YES")
    else:
        print("NO")

"""
1
5 3
1 3
2 3
4 5
"""
