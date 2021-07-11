import collections
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1): # 정렬을 해줘야 다음 bfs,dfs를 수행할때 숫자가 작은값부터 실행한다.
    graph[i].sort()

queue = collections.deque()


def bfs(index):
    queue.append(index)
    check[index] = True
    print(index, end=" ")
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if check[next] == False:
                print(next, end=" ")
                check[next] = True
                queue.append(next)
                
def dfs(index):
    check[index] = True
    print(index, end=" ")
    for next in graph[index]:
        if check[next] == False:
            dfs(next)

dfs(v)
check = [False for _ in range(n+1)]
print("")
bfs(v)