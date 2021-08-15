# dp 왤캐 어렵냐
# n = int(input())
# dp = [0 for _ in range(1001)]
# dp[1] = 10
# dp[2] = 55
# for i in range(3,n+1):    
#     for k in range(1, 10*(i-1) + 1):
#         dp[i] += k
#     dp[i] = dp[i] + dp[i-2]
# print(dp[n]%10007)


n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[n]) % 10007)

# 쉬운계단수와 유사..
#           0 1 2 3 4 5 6 7 8 9
# 자리수(1) 1 1 1 1 1 1 1 1 1 1
# 자리수(2) 1 2 3 4 5 6 7 8 9 10
# 자리수(3) 1 3 6 10 15 21 28 36 45 55 => 전체 배열합 220

# [i] = [i-1][j]까지에 전체합