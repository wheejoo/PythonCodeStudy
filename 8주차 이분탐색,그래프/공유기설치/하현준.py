"""
공유기 설치 https://www.acmicpc.net/problem/2110
pypy3 : 292ms
python3 : 5412ms
"""


def fn(param):
    count = 1
    gong = 0
    for i in range(1, n):
        if data[i] - data[gong] >= param:
            count += 1
            gong = i
    return count >= c


def search():
    lo = -1
    hi = data[-1] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2  # mid값은 data의 집의 좌표를 의미하는게 아니다.
        if fn(mid):
            lo = mid
        else:
            hi = mid
    return lo


n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

print(search())
