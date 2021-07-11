import sys
sys.setrecursionlimit(10 ** 9) #재귀 - 시간초과 해결

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


def DFS(v):
    visited.append(v)
    for i in range(1, n + 1):
        if (i not in visited) and (graph[v][i] == 1): #방문하지 않은 인접노드
            DFS(i)
            # print(DFS(i)) -> 3,6,7,8,8
    return (len(visited) - 1) #마지막 값이 한번 더 나오기 때문에 -1

print(DFS(1)) #1번컴퓨터바이러스 감염