# https://www.acmicpc.net/problem/2805

n,m = map(int,input().split())
height = list(map(int,input().split()))

def solution(m, height):
    left = 1
    right = max(height)
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        log = 0
        for h in height:
            if h > mid:
                log += h-mid
                # print(log)
        if log >= m:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(solution(m,height))



# def binary_search(i, list, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if i == mid:
#         return 1
#     elif i < mid:
#         return binary_search(i, list, start, mid-1)
#     else:
#         return binary_search(i, list, mid+1, end)

