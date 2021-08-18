'''
보자마자 느낌이 MST아니면 유니온파인드 느낌이 딱든다.
그렇다면 쉬운 크루스칼(유니온파인드)을 쓰악 써주면 될거같다.
'''
N = int(input())
M = int(input())
adj = []
for _ in range(M):
    a,b,c = map(int, input().split())
    adj.append([c,a,b])
adj.sort()# 거리별로 갱신된다.

# 이제 유니온파인드를 통해 하나씩 연결해주기~
parent = [i for i in range(N+1)]
def find(node):
    if node == parent[node]:# 자신의 노드다
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(node1,node2):
    parent1 = parent[node1]
    parent2 = parent[node2]
    parent[parent2] = parent1

cost = 0
for i in range(M):
    c,a,b = adj[i]
    if find(a) != find(b):
        cost += c
        union(a,b)
print(cost)