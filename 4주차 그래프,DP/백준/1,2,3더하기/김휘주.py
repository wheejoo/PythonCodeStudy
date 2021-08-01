# https://www.acmicpc.net/problem/9095

t = int(input())

# for _ in range(t):
#     n = int(input())
#     print(solution(n))

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

for _ in range(t):
    n = int(input())
    print(solution(n))

# 1 1 -1
# 2 1+1 2 -2
# 3 1+1+1 1+2 2+1 3 -4
# 4 1+1+1+1 1+1+2(3) 2+2 1+3(2) -7
# 5 1+1+1+1+1 1+1+1+2(4) 1+1+3(3) 1+2+2(3) 2+3(2) -13