# https://www.acmicpc.net/problem/1197
# 크루스칼?

v,e = map(int,input().split())
n = []
for _ in range(e):
    a,b,c = map(int,input().split())
    n.append((c,a,b)) #c는 가중치
n.sort() #가중치 순으로 정렬
parent = [0] * (v+1)
result = 0

# 특정 원소 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 자기자신을 초기화
for i in range(1, v+1):
    parent[i] = i

for edge in n:
    c,a,b = edge
    # 사이클이 발생하지 않으면 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c

print(result)