# dp 풀이가 안떠오른다..
t = int(input())

dp = [[0]*30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for i in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])

# from itertools import combinations
# import math
# t = int(input())

# for i in range(t):
#     n, m = map(int, input().split())
#     # result_m = [i for i in range(m)]
#     # com = list(combinations(result_m, n))
#     # print(len(com))
    
#     # combinations로 모든 조합 리스트를 구하면 시간초과가 난다.

#     # 왼쪽에 4개의 점, 오른쪽에 6개의 점이 있을때
#     # 4개에서 6개중에 4개를 선택한다.
#     # 자릿수는 4개가 나온다.
#     # 6개중에서 고른다.
#     # => 6개 리스트에서 4자리수 조합을 구한다.
#     print(math.comb(m,n))