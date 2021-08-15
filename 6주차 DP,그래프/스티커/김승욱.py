t = int(input())

for i in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for i in range(2, n):
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

        print(max(sticker[0][n-1], sticker[1][n-1]))
