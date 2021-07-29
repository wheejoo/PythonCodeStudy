
def dfs(node,n,st):

    visited = [0 for i in range(n+1)]
    s = [node]
    count = -1
    while s:
        target = s.pop()
        count+=1
        visited[target] = 1
        if visited[st[target]] == 0:
            s.append(st[target])
        if target == st[target]:
            return 0
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    st = [0] + list(map(int, input().split()))
    total = 0
    for i in range(1,n+1):
        print(dfs(i,n,st))
    print(n-total)

