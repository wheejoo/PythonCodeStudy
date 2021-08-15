# https://www.acmicpc.net/problem/2293
# 참고 https://mong9data.tistory.com/68

n, k = map(int, input().split())
c = []

for _ in range(n):
    c.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

for i in c:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])

# ex)5원 - 5원을 포함X 방법 + 5원 포함하는 방법