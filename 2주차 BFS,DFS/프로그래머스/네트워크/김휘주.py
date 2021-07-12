def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            answer += 1
            DFS(n, computers, com, visited)
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for con in range(n):
        if con != com and computers[com][con] == 1:
            if visited[con] == False:
                DFS(n, computers, con, visited)


n = 3
computers= [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))