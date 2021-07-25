import sys
input = sys.stdin.readline

n = int(input())
M=[]
for i in range(n):
    tmp = list(map(int, input().split()))
    M.append(tmp)
dp =[[1 for i in range(n)] for i in range(n)]

def DFS(i,j):
    s = [[i,j,1]]
    dy = [0,0,1,-1] #동서남북
    dx = [1,-1,0,0] #동서남북
    big = 0
    while s:
        y,x,z = s.pop()
        if z > big:
            big = z
        for i in range(4):
            ny  = y+dy[i]
            nx  = x+dx[i]
            if (0<=ny<n) and (0<=nx<n) and M[ny][nx] > M[y][x]:
                s.append([ny,nx,z+1])
    return big

for i in range(n):
    for j in range(n):
        print("a")


"""
시간초과
n = int(input())
M=[]
oM =[]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        oM.append([tmp[j],i,j])
    M.append(tmp)
oM.sort()

def DFS(i,j):
    s = [[i,j,1]]
    dy = [0,0,1,-1] #동서남북
    dx = [1,-1,0,0] #동서남북
    big = 0
    while s:
        y,x,z = s.pop()
        if z > big:
            big = z
        for i in range(4):
            ny  = y+dy[i]
            nx  = x+dx[i]
            if (0<=ny<n) and (0<=nx<n) and M[ny][nx] > M[y][x]:
                s.append([ny,nx,z+1])
        print(s)
    return big

def main():
    big = 0
    for t in oM:
        v,i,j = t
        print(v,i,j)
        if big > n*n-v-1:#시작부터 나올수 있는 최댓값
            return big
        tmp = DFS(i,j)
        if tmp > big:
            big = tmp
    return big
print(main())
"""