# https://www.acmicpc.net/problem/14501
# 참고 https://jrc-park.tistory.com/119?category=378936
# 참고했지만,,어렵...

n = int(input())
t = [0 for i in range(n+1)]
p = [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    t[i] = a #t[i] - 걸리는 일수
    p[i] = b #p[i] - 금액
    # print(t[i])
    # print(p[i])

dp =[0 for i in range(n+1)]

for i in range(len(t)-2, -1, -1):
    if t[i]+i <= n:       # 현재 + 걸리는 일수가 퇴사일을 초과 X
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])
    else:                 # 날짜 초과
        dp[i] = dp[i+1]
print(dp[0])