def solution(money):
    answer = 0
    dp = [0 for i in range(len(money))]
    dp2 = [0 for i in range(len(money))]
    dp[0] = money[0]
    dp[1] = money[0]#첫집 훔치는 경우
    dp[2] = money[0]#첫집 훔치는 경우
    
    dp2[0] = money[0]
    dp2[1] = money[1]#두번째 훔침
    dp2[2] = money[1]#두번째 훔침
    for i in range(3, len(money)):
        dp[i] = max(dp[i-2]+money[i-1] , dp[i-1])
        dp2[i] = max(dp2[i-2]+money[i] , dp2[i-1])

    return max(dp[-1],dp2[-1])
# t2, t4 실패, 원리를 정확히 이해를 못하겠음.