"""
최소 스패닝 트리 https://www.acmicpc.net/problem/1197
크루스칼
"""
import sys

input = sys.stdin.readline


def find_parent(pparent, x):
    if pparent[x] != x:
        pparent[x] = find_parent(pparent, pparent[x])
    return pparent[x]


def union_parent(pparent, pa, pb):
    pa = find_parent(pparent, pa)
    pb = find_parent(pparent, pb)
    if pa < pb:
        pparent[pb] = pa
    else:
        pparent[pa] = pb


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    # a-b 간선이 여러번 나올 경우 고려할 필요 없다.
    # 어차피 edges.sort() 하면 가중치가 가장 낮은 경우가 먼저 union_parent 됨
    edges.append((c, a, b))

edges.sort()  # cost 기준으로 오름차순 정렬
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# print(edges)
# print(" ".join(str(x) for x in range(v + 1)))
# print(" ".join(str(x) for x in parent))
print(result)
