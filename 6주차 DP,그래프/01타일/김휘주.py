# https://www.acmicpc.net/problem/1904

n = int(input())
dp = [0] * 10000001
# dp[0] = 0
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746

print(dp[n])

# n = 1 : 1
# n= 2 : 00 11
# n = 3 : 001 100 111
# n = 4 : 0000 0011 1100 1001 1111
# n = 5 : 00100 00111 11001 00001 10011 11111 11100 000001
# n = n-1 + n-2