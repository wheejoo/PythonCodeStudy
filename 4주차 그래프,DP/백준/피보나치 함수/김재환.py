t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[1,0],[0,1]]

    for i in range(2, n+1):
        dp.append([dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1]])
    for i in dp[n]:
        print(i, end=' ')
    print()