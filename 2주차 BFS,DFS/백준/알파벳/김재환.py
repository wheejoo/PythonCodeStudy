r, c = map(int, input().split())
M = []
for i in range(r):
    tmp = list(input())
    M.append(tmp)

alpha = [0]*26
alpha[ord(M[0][0])-65] = 1
s = [[[0, 0], alpha]]
count = 1
dx = [0, 0, 1, -1]  # 동서남북
dy = [1, -1, 0, 0]
while s:
    point, path = s.pop()
    print("point:", point)
    x, y = point
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < r) and (0 <= ny < c) and (path[ord(M[nx][ny])-65] == 0):
            newpath = list(path)
            newpath[ord(M[nx][ny])-65] = 1
            s.append([[nx, ny], newpath])
            if count < sum(newpath):
                count = sum(newpath)
    print(s)
print(count)
