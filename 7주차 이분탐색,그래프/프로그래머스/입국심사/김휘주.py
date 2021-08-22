# https://programmers.co.kr/learn/courses/30/lessons/43238
# 참고

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left < right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
            # print(total)
        if total >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer

n = 6
times = [7, 10]

print(solution(n, times))