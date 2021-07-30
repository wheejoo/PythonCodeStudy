import collections
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    distance = [0 for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    queue = collections.deque()
    queue.append(1)
    def bfs():
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for next in graph[cur]:
                if visited[next] == False:
                    visited[next] = True
                    distance[next] = distance[cur] + 1
                    queue.append(next)
    bfs()
    maxx = max(distance)
    for i in distance:
        if maxx == i:
            answer += 1
    return answer