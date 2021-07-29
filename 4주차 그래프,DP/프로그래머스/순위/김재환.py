# 플로이드 워셜 : 변의 가중치가 음수도 가능(음수사이클 없어야함.),  한번 수행하면 모든 꼭직점간의 최단 경로 구함.
# 방향성이 있는 경우 사용가능하다. dp의 특징인 메모리의 크기가 문제인데
# 주어진 N<= 100 이므로 100*100정도의 dp라 문제가 없다.
# 단, 여기서 중요한것은 서로의 최단거리를 구한다기 보다는 각자의 부모 자식간의 경계만 명확히 해준다.
# 그럼 inf를 제외하고는 전무 1 or -1이 되므로 부모자식 관계가 명확히 설정된 노드만 뽑아낼 수 있다.
def solution(n, results):
    inf = 100
    dp = [[inf for i in range(n+1)] for i in range(n+1)]
    for item in results:
        a,b = item
        dp[a][b] = 1 # 이긴 경우
        dp[b][a] = -1 # 진 경우
    
    # 플로이드는 키즈~ k i j
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j] == inf:
                    if dp[i][k] == 1 and dp[k][j] == 1: # 둘다 이긴경우 관계를 명확히 이겼다고 명시 가능
                        dp[i][j] = 1
                    if dp[i][k] == -1 and dp[k][j] == -1: # 자식이나 둘다 진경우 명확히 졌다고 명시 가능
                        dp[i][j] = -1
    flag = True
    count=0
    for i in range(1,n+1):
        flag = True
        for j in range(1,n+1):
            if i == j:#자기 자신인경우를 제외
                continue
            if dp[i][j] == inf:
                flag = False
                break
        if flag == True:
            count+=1
    return count

'''
BFS로 풀려했는데 안됨 -> 플로이드 워셜로 풀어야함.
from collections import deque
def solution(n, results):
    M = [[] for i in range(n+1)]
    child = [[]for i in range(n+1)]
    for i in range(len(results)):
        a,b = results[i]
        M[a].append(b)
        M[b].append(a)
        child[a].append(b)
    
    q = deque([])
    visited = [0 for i in range(n+1)]

    for i in range(1, n+1):
        if len(child[i]) == 0:
            q.append(i)
            visited[i] = 1
    print("q:",q)
    print("v:",visited)
    print("M:",M)
    # BFS
    count = 0
    while q:
        if len(q) == 1:
            count+=1
        for _ in range(len(q)):
            node = q.popleft()
            childlist = M[node]
            for child in childlist:
                if(visited[child] == 0):
                    q.append(child)
                    visited[child] = 1
        print(q)
    print(count)
    return count
'''