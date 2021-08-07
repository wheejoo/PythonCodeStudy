# https://songsunbi.tistory.com/80
# 거꾸로 하면 풀리는 문제였음.
# dp거꾸로 처음인데 참신했음.
n = int(input())
dp = [0 for i in range(n+1)]
t = []
p = []
for i in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1,-1,-1):
    if t[i] == 1: #일을 할수 있는 경우
        dp[i] = p[i] + dp[i+1]
    else: #일을 당장 못끝내는 경우
        if n < i + t[i]: # 범위를 넘어가는 경우
            dp[i] = dp[i+1]
        else: # 범위 내인경우
            dp[i] = max( dp[i+1], dp[i+t[i]] + p[i])
print(dp[0])