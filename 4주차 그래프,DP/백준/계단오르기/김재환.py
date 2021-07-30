n = int(input())
score = [0 for i in range(n+1)]
dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    score[i] = int(input())
if n >= 1 :
    dp[1] = score[1]
if n >= 2:
    dp[2] = score[2] + score[1]
if n >= 3:
    dp[3] = score[3] + max(score[2], score[1])

for i in range(4, n+1):
    dp[i] = score[i] + max(dp[i-2], dp[i-3]+score[i-1])
print(dp[n])
## 계단 건너뛰는거 살짝 어려웠다.