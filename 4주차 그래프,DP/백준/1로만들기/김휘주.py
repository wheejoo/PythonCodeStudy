# https://www.acmicpc.net/problem/1463
# 참고 https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0
#이해가 쫌,,

n = int(input())

def solution(n):
    dp = [0] * (n + 1)
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
    return dp[n]
print(solution(n))


#틀린버전,,,
# n = int(input())
# def solution(n):
#     cnt = 0
#     while True:
#         if n % 3 == 0:
#             n //= 3
#         elif n % 2 == 0:
#             n //= 2
#         else:
#             n -= 1
#         cnt += 1
#         if n == 1:
#             break
#     return cnt
# print(solution(n))