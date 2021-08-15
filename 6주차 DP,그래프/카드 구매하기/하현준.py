"""
카드 구매하기 https://www.acmicpc.net/problem/11052
"""
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = p[1]
for i in range(2, n + 1):
    temp = [p[i]]
    # 숫자 (1 ~ i-1)에서 오직 1개만 사용하여 i를 만드는 경우의 값
    for j in range(1, i + 1):
        temp.append(i // j)
    # (1,i-1), (2,i-2), .. 숫자 2개로 i를 만드는 경우의 값
    for k in range(1, i // 2 + 1):
        temp.append(dp[k] + dp[i - k])
    dp[i] = max(temp)

print(dp[n])
