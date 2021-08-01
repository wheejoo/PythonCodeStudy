# https://www.acmicpc.net/problem/2579
# 참고

n = int(input())
dp = [0] * 301
s = [0] * 301
for i in range(n):
    s[i] = int(input())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2]) #max(한칸뛴거, 두칸뛴거)

for i in range(3,n): #4번째 칸부터
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]) #이부분이 어렵...

print(dp[n-1])



