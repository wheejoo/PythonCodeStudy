'''
# 문제에서 최소스패닝트리하라고 알려줌
# 최소 스패닝 트리는 그래프 정점 연결할때 
# 가장 작은 가중치를 갖는 트리

가중치 음수 존재, 절댓값이 1,000,000

MST 최소 스패닝 트리를 구하는 방법은 크루스칼? 프림?
이중에 크루스칼이 쉬움. 고로 요걸로 ㄲ
1. 우선순위 큐(최소힙)에 가중치 작은순으로 넣어줌
2. 하나씩 꺼내서 유니온 파인드함

'''
import sys
import heapq 
input = sys.stdin.readline

q = []
V,E = map(int, input().split())
parent = [ i for i in range(V+1)]

def find(node):
    if node == parent[node]:# 루트노드이면 반환
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    parent[parent2] = parent1

for _ in range(E):
    A,B,C = map(int, input().split())
    heapq.heappush(q, [C,A,B])

weight = 0
num = 1
while num != V:
    C,A,B = heapq.heappop(q)
    if find(A) == find(B): # 이미 같은 집합
        continue
    else:# 다른 집합인경우
        union(A,B)
        weight += C
        num+=1

print(weight)
