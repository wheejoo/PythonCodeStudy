n,k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp= [0 for i in range(k+1)]
dp[0] = 1
# 코인 초기화
for i in range(1, k+1):
    if i % coin[0] == 0:
        dp[i] += 1

# 코인 dp시작
for ci in range(1,n):
    for i in range(1, k+1):
        if i - coin[ci] >= 0:
            dp[i] = dp[i] + dp[i-coin[ci]]
print(dp[-1])

