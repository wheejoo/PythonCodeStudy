"""
퇴사 https://www.acmicpc.net/problem/14501
"""
n = int(input())
dp = [0 for _ in range(n + 1)]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in reversed(range(n)):
    term, price = data[i]
    if i + term <= n:
        dp[i] = max(dp[i + 1], dp[i + term] + price)
    else:
        dp[i] = dp[i + 1]

print(dp[0])
