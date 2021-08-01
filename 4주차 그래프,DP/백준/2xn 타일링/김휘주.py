# https://www.acmicpc.net/problem/11726

n = int(input())
dp = [0] * (n+1)
def solution(n):
    if n <= 3:
        return n
    else:
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return (dp[i] % 10007)
print(solution(n))

# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5

# 시간초과...
# import sys
# sys.setrecursionlimit(1000000)
#
# n = int(input())
#
# def solution(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return solution(n-2) + solution(n-1)
# answer = solution(n)
# print(answer % 10007)