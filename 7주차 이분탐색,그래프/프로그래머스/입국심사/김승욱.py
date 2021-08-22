# 접근법을 생각 못헀던 문제..
def solution(n, times):
    answer = 0
    l = 1
    r = max(times) * n
    
    check = 0
    while l <= r:
        answer = 0
        mid = (l+r) // 2
        
        for i in times:
            answer += mid // i
        
        if answer >= n:
            r = mid - 1
            check = mid
        else:
            l = mid + 1
    return check