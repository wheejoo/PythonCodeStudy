N = int(input())
Tmp = []
for _ in range(N):
    Tmp.append(list(map(int, input().split())))

print(Tmp)


def DFS(n, start, visited):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    s = [start]
    while s:
        y, x = s.pop()
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N) and (0 <= nx < N):  # 인덱스 기준
                if Tmp[ny][nx] >= n and visited[ny][nx] == 0:
                    s.append([ny, nx])
    # N잡고 기준으로 DFS실시 -> 총 DFS 개수를 비교


big = 0
for n in range(1, 101):  # N 기준
    visited = [[0 for i in range(N)] for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and Tmp[i][j] >= n:
                DFS(n, [i, j], visited)
                count += 1
    print(n, count)
    if big < count:
        big = count
print(big)
