from collections import deque
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution(a,b):
    answer = 1
    q = deque([(a,b,graph[a][b])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ans:
                q.append((nx,ny,ans+graph[nx][ny]))
                answer = max(answer, len(ans)+1)
    return answer

print(solution(0,0))
