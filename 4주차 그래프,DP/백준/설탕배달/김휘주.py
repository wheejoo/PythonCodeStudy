# https://www.acmicpc.net/problem/2839

n = int(input())

def solution(n):
    cnt = 0
    while True:
        if n % 5 == 0:
            cnt += (n//5)
            break
        n -= 3
        cnt += 1
        if n < 0:
            return -1
    return cnt

print(solution(n))

