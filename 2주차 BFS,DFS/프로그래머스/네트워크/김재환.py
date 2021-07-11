def dfs(n, i,computers,visited):
    s = [i]
    while s:
        t = s.pop()
        visited[t] = 1
        ts = computers[t]
        for i in range(n):
            if i != t:#뽑은 t와 인덱스가 달라야함
                if ts[i] == 1 and visited[i] == 0: #연결된경우 stack에 저장
                    s.append(i)
    return 1
                    
                
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            answer += dfs(n,i,computers,visited)
    return answer