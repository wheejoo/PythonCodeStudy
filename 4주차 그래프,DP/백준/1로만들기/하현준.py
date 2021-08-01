"""
1로 만들기 https://www.acmicpc.net/problem/1463
"""
n = int(input())
if n == 1:
    print(0)
    exit(0)
elif n == 2 or n == 3:
    print(1)
    exit(0)
dp = [-1 for _ in range(n + 1)]
dp[1], dp[2], dp[3] = 0, 1, 1
for i in range(4, n + 1):
    temp = dp[i - 1] + 1  # '-1'연산 횟수를 temp 담는다
    if i % 2 == 0:  # temp = min('-1' 연산 횟수, '2나누기' 연산횟수)
        temp = min(temp, dp[i // 2] + 1)
    if i % 3 == 0:  # temp = min('2나누기' 연산 횟수, '3나누기' 연산횟수)
        temp = min(temp, dp[i // 3] + 1)
    dp[i] = temp

print(dp[n])
