import collections
def solution(n, computers):
    
    def bfs(index):
        count = -1
        check[index] = True
        queue = collections.deque()
        queue.append(index)
        while queue:
            count += 1
            cur = queue.popleft()
            for next in graph[cur]:
                if check[next] == False:
                    check[next] = True
                    queue.append(next)
        return count
    
    answer = 0
    graph = [[] for _ in range(n+1)]
    check = [False for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
    
    for i in range(len(graph)):
        if graph[i] and check[i] == False:
            answer += bfs(i)
            print(answer)
            
    return len(computers) - answer