# https://www.acmicpc.net/problem/2252
# 위상,,정렬 - 선후관계 파악 
# 참고 - 이것이 코딩테스트다,, 책,,

from collections import deque

v,e = map(int,input().split())
n = [0] * (v+1) #노드에 대한 차수 0으로 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b) # a -> b
    n[b] += 1 #차수 +1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1): #차수가 0인것부터 시작
        if n[i] == 0: #차수가 0이면
            q.append(i) #q에 append

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]: #원소와 연결된 노드 차수 -1
            n[i] -= 1
            if n[i] == 0: #차수가 0이면
                q.append(i) #q에 append

    for i in result:
        print(i, end = " ")

topology_sort()

