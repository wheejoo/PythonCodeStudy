# https://www.acmicpc.net/problem/1922

n = int(input()) #컴퓨터 수 - 노드
m = int(input()) #연결 수 - 간선

edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
result = 0

for i in range(1, n+1):
    parent[i] = i

edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)