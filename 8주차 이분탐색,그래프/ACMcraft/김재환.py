"""
DAG 위상정렬을 사용하는거 같은 느낌 어렵다.
1. adj와 위상정렬용 memo 구하기
2. BFS로 위상정렬 시작한다.
3. 추가적으로 dp를 돌리면서 점화식을 돌린다.
4. 목표 노드에 도착하면 루프 종료시킨다.
5. 해당 값을 반환한다.
=> 와 이거 알고리즘 분류 힌트 안봤으면 못풀었을거 같다
=> DP는 역시 어렵
"""
import sys
input = sys.stdin.readline

def staller():
    N,K = map(int, input().split())
    cost = [0] + list(map(int, input().split())) # cost설정
    adj = [[] for i in range(N+1)]
    memo = [ 0 for i in range(N+1)]
    for _ in range(K):
        a,b = map(int, input().split())
        adj[a].append(b)
        memo[b] += 1
    W = int(input())

    from collections import deque
    q = deque([])
    for i in range(1, N+1): # 시작할 노드들을 찾는다.
        if memo[i] == 0:
            q.append(i)
    # BFS로 위상정렬 시작하기
    dp = [-1 for i in range(N+1)]
    for i in q:
        dp[i] = cost[i]

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == W:
                q = []
                break
            childs = adj[node]
            for child in childs:
                if dp[child] == -1:# 갱신이 된적 없음
                    dp[child] = dp[node] + cost[child]
                else:
                    if dp[child] < dp[node] + cost[child]:
                        dp[child] = dp[node] + cost[child]
                memo[child] -= 1
                if memo[child] == 0:
                    q.append(child)
    print(dp[W])
T = int(input())
for _ in range(T):
    staller()