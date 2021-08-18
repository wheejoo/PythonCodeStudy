"""
수 찾기 https://www.acmicpc.net/problem/1920
"""


def search(target):
    low = -1
    high = n
    while low + 1 < high:
        mid = (low + high) // 2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            high = mid
        else:
            low = mid
    return 0


n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))
for t in mlist:
    print(search(t))
