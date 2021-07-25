# https://programmers.co.kr/learn/courses/30/lessons/42895

N = 5
number = 12
# N = 2
# number = 11
def solution(N, number):
    # for i in range(1,9):
    #     s = set()
    #     s.add(int(str(N)*i))
    # dp = [set(int(str(N)*i)) for i in range(1,9)] #에러
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    # print(dp) #[{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    for i in range(8): #1~8
        for j in range(i):
            for n1 in dp[j]: #i번
                for n2 in dp[i-j-1]: #n-i번
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)
        if number in dp[i]: #n을 i번 사용
            answer = i+1
            break
    else:
        answer = -1
    return answer

print(solution(N,number))