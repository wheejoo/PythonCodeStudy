n = int(input())
M = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = M[0]
for i in range(1, n):
    dp[i] = max(M[i], M[i]+dp[i-1])
print(max(dp))
# 이차면 시간복잡도가 N^2이라 10,000에서 시간초과남
# N으로 줄여야함.
'''
n = int(input())
M = [0] + list(map(int, input().split()))
dp = [0 for i in range(n+1)]
big = 0
for i in range(1, n+1):
    dp[i] = M[i]
    for j in range(i+1,n+1):
        dp[j] = dp[j-1] + M[j]
    big = max(big, max(dp))
print(big)
'''