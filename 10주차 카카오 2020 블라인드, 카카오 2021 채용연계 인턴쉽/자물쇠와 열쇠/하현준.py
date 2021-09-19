"""
자물쇠와 열쇠
https://programmers.co.kr/learn/courses/30/lessons/60059
"""


def rotate(m, data):
    rdata = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rdata[j][m - i - 1] = data[i][j]
    return rdata


def check(x, y, n, m, key, nlock):
    flag = True
    for i in range(x, x + m):
        for j in range(y, y + m):
            nlock[i][j] += key[i - x][j - y]

    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if nlock[i][j] != 1:
                flag = False
                break
        if not flag:
            break

    for i in range(x, x + m):
        for j in range(y, y + m):
            nlock[i][j] -= key[i - x][j - y]
    return flag


def solution(key, lock):
    m = len(key)
    n = len(lock)
    nlock = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            nlock[i][j] = lock[i - n][j - n]

    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            for k in range(4):
                if check(i, j, n, m, key, nlock):
                    return True
                key = rotate(m, key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
