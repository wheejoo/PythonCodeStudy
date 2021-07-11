from collections import deque
#수빈 현재점 n, 동생 현재점 k
n,k = map(int,input().split())
visited = [False] * 100001

def bfs(n):
    cnt = 0
    q = deque([[n,cnt]])
    while q:
        v = q.popleft()
        current = v[0] #현재
        cnt = v[1]
        if not visited[current]: #방문하지 X
            visited[current] = True #방문
            if current == k: #동생위치와 같으면
                return cnt #그때의 cnt
            cnt += 1 #그게 아니면 +1
            # (0<=N<=100000) (0<=K<=100000)
            if (current-1) >= 0:
                q.append([current-1,cnt])
            if (current+1) <= 100000:
                q.append([current+1,cnt])
            if (2*current) <= 100000:
                q.append([2*current,cnt])
    return cnt

print(bfs(n))


