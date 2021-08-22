# https://www.acmicpc.net/problem/1654

k,n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))

def solution(n, line):
    left = 1
    right = max(line)
    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        log = 0
        for l in line:
            log += l // mid
            # log += l - mid
            # print(log)
        if log >= n:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(solution(n, line))



# def binary_search(i, list, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if i == mid:
#         return 1
#     elif i < mid:
#         return binary_search(i, list, start, mid+1)
#     else:
#         return binary_search(i, list, mid-1, end)

