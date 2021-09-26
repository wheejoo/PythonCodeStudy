"""
퇴사
https://www.acmicpc.net/problem/14501
"""
n = int(input())
dp = [0 for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(n)]

for day in reversed(range(n)):
    time, price = data[day]
    if day + time < n:
        dp[day] = price + max(dp[day + time:])
    elif day + time == n:
        dp[day] = price

print(max(dp))
