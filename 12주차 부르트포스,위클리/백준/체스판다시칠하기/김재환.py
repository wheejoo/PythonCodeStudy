N, M = map(int, input().split())

Map = []
for i in range(N):
    Map.append(list(input()))

print(Map)

# 시작점
small = N*M
for i in range(0, N-7):
    for j in range(0, M-7):
        # 연산 시작~ W시작하는경우
        num = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                print(y, x)
                next = (y-i) + (x-j)
                if next % 2 == 0:  # 시작과 동일해야함
                    if Map[y][x] != 'W':
                        num += 1
                else:  # 달라야함
                    if Map[y][x] == 'W':
                        num += 1
        # 'B'로 시작하는 경우
        num2 = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                next = (y-i) + (x-j)
                if next % 2 == 0:
                    if Map[y][x] != 'B':
                        num2 += 1
                else:  # 달라야함
                    if Map[y][x] == 'B':
                        num2 += 1
        s = min(num, num2)
        if s < small:
            small = s
print(small)
