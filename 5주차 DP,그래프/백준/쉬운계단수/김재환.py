#이걸 도대체 어떻게 생각해내는거지?
n=int(input())
dp =[[0 for i in range(10)] for i in range(101)]
for i in range(1,10):
    dp[0][i] = 1
for i in range(1, n):
    for j in range(10):
        if j ==0:
            dp[i][j] += dp[i-1][j+1]
            continue
        if j == 9:
            dp[i][j] += dp[i-1][j-1]
            continue
        dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n-1])%1000000000)


'''n=int(input())

graph = [1,2,3,4,5,6,7,8,9]
dp = [0,0,0,0,0,0,0,0,0,0]
dp2 = [0,0,0,0,0,0,0,0,0,0]
for _ in range(1,n):
    tmp = []
    for i in range(len(graph)):
        if graph[i] == 0:
            tmp.append(graph[i]+1)
            continue
        if graph[i] == 1:
            dp[_] += 1
        if graph[i] == 9:
            tmp.append(graph[i]-1)
            dp2[_] += 1
            continue
        tmp.append(graph[i]-1)
        tmp.append(graph[i]+1)
    graph = tmp

print(dp)
print(dp2)

print(len(graph)%1000000000)
'''