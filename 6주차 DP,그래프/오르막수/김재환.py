n = int(input())

dp = [1 for i in range(10)]

for _ in range(1, n):
    for i in range(10):
        dp[i] = sum(dp[i:])
print(sum(dp)%10007) 
#마지막에 %10007