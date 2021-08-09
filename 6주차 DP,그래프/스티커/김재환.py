t = int(input())
for _ in range(t):
    n = int(input())
    score = []
    for i in range(2):
        score.append(list(map(int, input().split())))

    dp = [[0 for i in range(n)] for i in range(2)]
    for i in range(n):
        if i == 0:
            dp[0][i] = score[0][i]
            dp[1][i] = score[1][i]
        elif i == 1:
            dp[0][i] = score[0][i] + dp[1][i-1]
            dp[1][i] = score[1][i] + dp[0][i-1]
        else:
            # 자신 포함 사이드 최대
            # 자신 포함 
            dp[0][i] = score[0][i]+ max(dp[1][i-1], max(dp[0][i-2],dp[1][i-2]))
            dp[1][i] = score[1][i]+ max(dp[0][i-1], max(dp[0][i-2],dp[1][i-2]))
    print(max(dp[0][n-1],dp[1][n-1]))