"""
네트워크 연결 https://www.acmicpc.net/problem/1922
"""


def find_parent(pp, x):
    if pp[x] != x:
        pp[x] = find_parent(pp, pp[x])
    return pp[x]


def union_parent(pp, a, b):
    a = find_parent(pp, a)
    b = find_parent(pp, b)
    if a < b:
        pp[b] = a
    else:
        pp[b] = a


n = int(input())
m = int(input())
result = 0
parent = [i for i in range(n + 1)]
data = []
for _ in range(m):
    a, b, c = map(int, input().split())
    data.append([c, a, b])

data.sort()
for cost, a, b in data:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
