"""
숫자 카드 2 https://www.acmicpc.net/problem/10816
bisect_left, bisect_right 함수를 외우자
pypy3 : 1584ms
python3 : 시간초과

그냥 dictionary 사용하는게 더 빠르네...
from collections import defaultdict
hashmap = defaultdict(int)
for d in data:
    hashmap[d] += 1
for t in target:
    print(str(hashmap[t]) + " ")

python3 : 1536ms
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


def search_left(num):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        temp = data[mid]
        if temp < num:
            lo = mid + 1
        elif temp >= num:
            hi = mid
    return lo


def search_right(num):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        temp = data[mid]
        if temp > num:
            hi = mid
        else:
            lo = mid + 1
    return lo


n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
target = list(map(int, input().split()))

for t in target:
    print(str(search_right(t) - search_left(t)) + " ")

