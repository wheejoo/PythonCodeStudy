n = int(input())
dp = [1 for i in range(n)]
M = list(map(int,input().split()))
for i in range(1, n):
    for j in range(i-1,-1,-1):
        if M[j] < M[i] :
            dp[i] = max(dp[j] + 1,dp[i])
print(dp)
print(max(dp))