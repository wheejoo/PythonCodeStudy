import collections
def solution(places):
    answer = []
    dx, dy = [-1, 1, 0, 0], [0,0,-1,1]
    def bfs(a,b,graph):
        visited = [[False]*5 for _ in range(5)]
        queue = collections.deque()
        queue.append((a,b))
        visited[a][b] = True
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if abs(a-nx) + abs(b-ny) <= 2 and graph[nx][ny] == 'O' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                    elif abs(a-nx) + abs(b-ny) <= 2 and graph[nx][ny] == 'P' and visited[nx][ny] == False:
                        
                        return False
        return True
        
    def tuto(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    flag = bfs(i,j,place)
                    if not flag:
                        return False
        return True
    
    for place in places:
        flag = tuto(place)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
                        
    return answer