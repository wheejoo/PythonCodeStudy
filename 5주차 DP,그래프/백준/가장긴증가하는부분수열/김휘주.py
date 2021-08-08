# https://www.acmicpc.net/problem/11053

n = int(input())
a = list(map(int,input().split()))
dp = [0] * n
def solution():
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    return max(dp)

print(solution())
