# https://programmers.co.kr/learn/courses/30/lessons/42898

m = 4
n = 3
puddles = [[2,2]]


def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)] #m,n -> index out of range
    # print(dp)
    dp[1][1] = 1 #집
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            # elif [i,j] in puddles: #물웅덩이 0
            elif [j,i] in puddles:
                #[i,j]여도 값은 4.. 왜 [j,i]로 해야 통과할까,,,
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j])
    return dp[-1][-1] % 1000000007

print(solution(m,n,puddles))