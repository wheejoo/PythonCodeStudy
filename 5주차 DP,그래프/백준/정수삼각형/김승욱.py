n = int(input())

circle = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(circle[i])):
        if j == 0:
            circle[i][0] += circle[i-1][0]
        elif j == len(circle[i])-1:
            circle[i][j] += circle[i-1][j-1]
        else:
            circle[i][j] += max(circle[i-1][j-1], circle[i-1][j])

print(max(circle[n-1]))