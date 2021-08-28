"""
예산 https://www.acmicpc.net/problem/2512
pypy3 : 140ms
python3 : 92ms
"""


def fn(param):
    return m >= sum([param if i > param else i for i in data])


def search():
    lo = 0
    hi = data[-1] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        result = fn(mid)
        print(f"lo={lo} mid={mid} hi={hi} {result}")
        if result:
            lo = mid
        else:
            hi = mid
    return lo


n = int(input())
data = list(map(int, input().split()))
m = int(input())
data.sort()
print(search())
