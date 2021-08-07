dp = [[1],[1,1],[1,2,1]]
for i in range(3,31):
    tmp = []
    for j in range(0,i+1):
        if j==0 or j==i:
            tmp.append(1)
            continue
        tmp.append(dp[i-1][j-1]+dp[i-1][j])
    dp.append(tmp)
# 이항계수 dp로 풀라는 소리였습니다~
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(dp[m][n])