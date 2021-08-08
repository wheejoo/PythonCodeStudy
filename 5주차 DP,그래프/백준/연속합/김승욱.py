n = int(input())
total = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = total[0]
for i in range(1, n):
    dp[i] = max(total[i] + dp[i-1], total[i])
print(max(dp))