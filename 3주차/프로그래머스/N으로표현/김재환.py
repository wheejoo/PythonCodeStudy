from time import sleep

def solution(N, number):
    answer = 0
    dp = [{}]
    for i in range(1, 9):
        dp.append({int(str(N)*i)})
        for a in range(1,i):
            for x in dp[a]:
                for y in dp[i-a]:
                    dp[i].add(x+y)
                    if x>=y:
                        dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0 and x/y == int(x/y): # 나누기라 0이 아니어야함
                        dp[i].add(x/y)
        sleep(1)
        print(dp)
        if number in dp[i]:
            return number
    print(dp)
    return -1
print(solution(5,12))