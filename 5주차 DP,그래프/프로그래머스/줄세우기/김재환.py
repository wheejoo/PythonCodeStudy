# 위상정렬 = 어떤 일을 하는 순서를 찾는 알고리즘
# 인접배열, 위상정렬용 배열, 탐색용 q배열, 최종 total배열 사용
# 아주 어렵다.

from collections import deque
n,m = map(int, input().split())
graph = [[]for i in range(n+1)]
numMap = [0 for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
    numMap[b] += 1

q = deque([])
# q에 탐색할 노드를 넣어준다.
for i in range(1,n+1):
    if numMap[i] == 0:
        q.append(i)

total = []
while q:
    t = q.popleft()
    total.append(t)
    childs = graph[t]
    for child in childs:
        if numMap[child] == 0:
            continue
        else:
            numMap[child] -= 1
            if numMap[child] == 0:
                q.append(child)
for i in total:
    print(i, end=' ') 