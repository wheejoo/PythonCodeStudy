"""
랜선 자르기 https://www.acmicpc.net/problem/1654
"""


def fn(param):
    return sum([i // param for i in data])


def search():
    lo = 0
    hi = data[-1] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        temp = fn(mid)
        print(f"lo={lo} mid={mid} hi={hi} temp={temp}")
        if temp >= n:
            lo = mid
        else:
            hi = mid
    return lo


k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
data.sort()
print(search())
