def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            answer += 1
            DFS(n, computers, i, visited)
    return answer

def DFS(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if j != i and computers[i][j] == 1:
            if visited[j] == False:
                DFS(n, computers, j, visited)


n = 3
computers= [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))