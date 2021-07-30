n = int(input())
dp= [0 for i in range(n+1)]
if n>1:
    dp[2] = 1
if n>2:
    dp[3] = 1
for i in range(4, n+1):
    # dp[i] 를 구하기 위해 dp[i]-1, dp[i/2]*3, dp[i/3]*2 구하기
    tmp = []
    if i % 2 == 0:
        tmp.append(dp[int(i/2)]+1)
    if i % 3 == 0:
        tmp.append(dp[int(i/3)]+1)
    tmp.append(dp[i-1]+1)
    dp[i] = min(tmp)
print(dp[n])