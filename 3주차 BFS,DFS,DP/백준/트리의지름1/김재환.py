#### 다익스트라로 풀었지만 메모리 초과로 안됨
#### 다른거 보니까 트리인 경우에는 굳이 다익스트라로 풀어서 좋을게 없음. 
#### 따라서 트리인 경우에는 dfs, bfs를 사용하여 해결해야한다.
### 이 문제는 다익스트라 없이 가능한데 이유는 우선 트리에서 가장 깊고 가중치가 높은 노드를 찾는다.
### 이후에 그 leaf노드를 정점으로 가장 깊고 가중치가 높은 노드를 찾는다.
import sys
input = sys.stdin.readline

n = int(input())
M =[[]for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    M[a].append([b,c])
    M[b].append([a,c])

def DFS(node):
    s = [[node,0]]
    visited = [0 for i in range(n+1)]
    big = 0
    leaf = 0
    while s:
        node,length = s.pop()
        visited[node] = 1
        nodelist = M[node]
        if len(nodelist) == 1: #leaf노드일경우 length를 big와 비교
            if length > big:
                big = length
                leaf = node
        for node in nodelist:
            if visited[node[0]] == 0:
                s.append([node[0],node[1]+length])

    return leaf, big
node,legth = DFS(1)
node,legth = DFS(node)
print(legth)

'''
import sys
input = sys.stdin.readline
n = int(input())
M =[[]for i in range(n+1)]
W = [[0 for i in range(n+1)] for i in range(n+1)]

from time import sleep
for i in range(n-1):
    a,b,c = map(int, input().split())
    M[a].append(b)
    M[b].append(a)
    W[a][b] = c
    W[b][a] = c

def DFS(left, mid, right):
    print("l,m,r",left, mid, right)
    print( W[left][right],W[left][mid] ,W[mid][right])
    W[left][right] = W[left][mid] + W[mid][right]
    print( W[left][right],W[left][mid] ,W[mid][right])

    childnode = M[right]
    print("child", childnode)
    for child in childnode:
        if left == child or mid == child:
            continue
        DFS(left, right, child)

for start in range(1,n+1):
    childnode = M[start]
    for child in childnode:
        DFS(start, start, child)

big = 0
for i in range(n):
    if big < max(W[i]):
        big =max(W[i])
print(big)    
'''