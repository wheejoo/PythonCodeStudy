import collections
n, k = map(int, input().split())
MAX = 200000
queue = collections.deque()
queue.append(n)
distance = [0] * (MAX+1)

def bfs():
    
    while queue:
        cur = queue.popleft()
        if cur == k:
            break
        for move in [cur+1, cur-1, cur*2]:
            if 0 <= move <= MAX and distance[move] == 0:
                distance[move] = distance[cur] + 1
                queue.append(move)

bfs()
print(distance[k])


