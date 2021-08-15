"""
쉬운 계단 수 https://www.acmicpc.net/problem/10844
dp[0]  0 0 0 0 0 0 0 0 0 0
dp[1]  0 1 1 1 1 1 1 1 1 1
dp[2]  1 1 2 2 2 2 2 2 2 1

"""
n = int(input())
num = 10 ** 9
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for k in range(1, 9):
        dp[i][k] = dp[i - 1][k - 1] + dp[i - 1][k + 1]
print(sum(dp[n]) % num)

for i in range(1, len(dp)):
    print(f"dp[{i}] ", " ".join([str(x) for x in dp[i]]), sum(dp[i]))
