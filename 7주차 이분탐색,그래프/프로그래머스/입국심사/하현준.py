"""
입국심사 https://programmers.co.kr/learn/courses/30/lessons/43238
참고 : https://wwlee94.github.io/category/algorithm/binary-search/immigration/
solution(6, [7,10]) : 28
solution(6, [6,10]) : 24
solution(6, [8,10]) : 30
solution(6, [4,10]) : 20
solution(11, [3,4,10]) : 18
solution(5, [1,1,10]) : 3
solution(3, [1, 1, 1] ) : 1
solution(3, [1, 2, 3] ) : 2
"""


def fn(param, times, n):
    count = 0
    for time in times:
        count += param // time
        if count >= n:
            break
    return count


def solution(n, times):
    times.sort()

    lo = 0
    hi = times[-1] * n + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        temp = fn(mid, times, n)
        if temp >= n:
            hi = mid
        else:
            lo = mid
    return lo + 1


print(solution(6, [7, 10]))
print(solution(6, [6, 10]))
print(solution(6, [8, 10]))
print(solution(6, [4, 10]))
print(solution(11, [3, 4, 10]))
print(solution(5, [1, 1, 10]))
print(solution(3, [1, 1, 1]))
print(solution(3, [1, 2, 3]))

