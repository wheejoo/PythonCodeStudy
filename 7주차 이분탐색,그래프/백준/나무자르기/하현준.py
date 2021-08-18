"""
나무 자르기 https://www.acmicpc.net/problem/2805
"""


def fn(param):
    return sum([i - param if i - param > 0 else 0 for i in data])


def search():
    lo = 0
    hi = data[-1] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        temp = fn(mid)
        print(f"lo={lo} mid={mid} hi={hi} temp={temp}")
        if temp >= m:
            lo = mid
        else:
            hi = mid
    return lo


n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
print(search())
