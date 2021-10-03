"""
pypy3로만 제출됨....
혹시 다른 방법 있으면 배우면 좋을듯
"""
N = int(input())

count = 0


def check(q, row, col):
    for i in range(row):
        # 열이 중복되는지
        if q[i] == col:
            return False
        # 크로스가 중복되는지 행과 열의 차가 동일
        if abs(q[i] - col) == abs(i - row):
            return False
    return True


def queen(q, row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if check(q, row, col):
            q[row] = col
            queen(q, row+1)


q = [0 for i in range(N)]
for i in range(N):
    q[0] = i
    queen(q, 1)
print(count)
