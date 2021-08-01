# https://programmers.co.kr/learn/courses/30/lessons/49189
# 참고 https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%EB%A8%BC-%EB%85%B8%EB%93%9C-%EA%B7%B8%EB%9E%98%ED%94%84

from collections import deque
def solution(n, vertex):
    # answer = 0
    graph = {}
    visited= [0] * n
    for e in vertex:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        graph[e[1]] = graph.get(e[1], []) + [e[0]]
    # print(graph) {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
    q = deque()
    q.append(1) #1번노드
    visited[0] = 1 #1번노드
    while q:
        node = len(q)
        for i in range(node):
            # print(q)
            v = q.popleft()
            # print(v)
            for j in graph[v]:
                if visited[j-1] == 0:
                    visited[j-1] = 1
                    q.append(j)
    return node

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))