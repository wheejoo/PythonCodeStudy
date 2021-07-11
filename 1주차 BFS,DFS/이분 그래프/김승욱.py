import collections
t = int(input())

def bfs(index):
    queue.append(index)
    check[index] = 1
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if check[nx] == 0:
                check[nx] = -1 * check[x]
                queue.append(nx)
            elif check[nx] == check[x]: # 값이 같으면 이분그래프가 아니다.
                return 1
    return 0

for i in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    check = [0 for _ in range(v+1)]

    for i in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    queue = collections.deque()
    ans = 0
    for i in range(1, v+1):
        if check[i] == 0:
            ans = bfs(i)
            if ans == 1:
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")