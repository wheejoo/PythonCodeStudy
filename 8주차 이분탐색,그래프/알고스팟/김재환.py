"""
최단거리를 찾는게 아닌 최소 벽을 부수는 경우를 찾기
만약 벽을 부수는 것을 1로 생각한다면 각 빈방은 0의 가중치를 갖는다.
단일 시작점 알고리즘이므로 다익스트라 or 벨만
음수 없으므로 다익스트라 ㄱㄱㅆ
"""

M,N = map(int, input().split()) # 가로 세로
Map = []
for _ in range(N):
    Map.append(list(map(int, input())))

# DFS로 adj 만들기
dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]

adj = [[] for i in range(N*M+1)]
visited = [[0 for i in range(M)] for i in range(N)]
s = [(0,0)]
def node_num(y,x):
    return y*M + x + 1

while s:
    y,x = s.pop()
    ori_node = node_num(y,x)
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<=ny<N) and (0<=nx<M) and visited[ny][nx] == 0:
            next_node = node_num(ny,nx)
            if Map[y][x] == 0 and Map[ny][nx] == 0: 
                adj[ori_node].append((next_node,0))
                adj[next_node].append((ori_node,0))
            elif Map[y][x] == 0 and Map[ny][nx] == 1: 
                adj[ori_node].append((next_node,1))
                adj[next_node].append((ori_node,0))
            elif Map[y][x] == 1 and Map[ny][nx] == 0: 
                adj[ori_node].append((next_node,0))
                adj[next_node].append((ori_node,1))
            else:
                adj[ori_node].append((next_node,1))
                adj[next_node].append((ori_node,1))
            s.append((ny,nx))

# 다익스트라 pq로 실행
INF = 1000*1000
dp = [INF for i in range(N*M+1)]
import heapq # 최소힙 구현
pq = [(0,1)] # 가중치, 노드
dp[1] = 0

while pq:
    cost, node = heapq.heappop(pq)
    if dp[node] < cost:
        continue

    for i in range(len(adj[node])):
        end, end_cost = adj[node][i]
        if dp[end] > cost+end_cost:
            dp[end] = cost+end_cost
            heapq.heappush(pq,(dp[end],end))

print(dp[-1])
    
