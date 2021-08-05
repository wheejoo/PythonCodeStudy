# 완전히 이해 잘 안됨.
n= int(input())
M = [0]
for _ in range(n):
    M.append(int(input()))
# 계단처럼 초기화해줘야함.
dp = [0 for i in range(n+1)]
dp[0] = M[1]
if n>1:
    dp[1] = M[1]+M[2]
if n>2:
    dp[2] = M[3] + max(M[2],M[1])
for i in range(3,n+1):
    dp[i] = max(dp[i-1], dp[i-3]+M[i-1]+M[i], dp[i-2]+M[i])
print(dp[-1])
