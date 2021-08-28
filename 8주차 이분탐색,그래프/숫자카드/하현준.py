"""
숫자 카드 https://www.acmicpc.net/problem/10815
pypy3 : 1064ms
python3 : 2612ms
"""
import sys

input = sys.stdin.readline


def search(num):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        temp = data[mid]
        if temp == num:
            return 1
        elif temp > num:
            hi = mid
        else:
            lo = mid + 1

    return 0


n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
target = list(map(int, input().split()))

for t in target:
    print(search(t), end=" ")
