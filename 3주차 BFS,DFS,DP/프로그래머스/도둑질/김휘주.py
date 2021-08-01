# https://programmers.co.kr/learn/courses/30/lessons/42897
##참고
#(i-1)번째 집을 털었 -> table[i-1]
#(i-1)번째 집을 안 털었 -> talbe[i-2] + money[i]

def solution(money):
    #첫번째 집을 털었
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    #첫번째 집을 안털었
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(1, len(money) - 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])
    answer = max(max(dp1), max(dp2))
    return answer