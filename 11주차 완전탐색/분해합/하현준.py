"""
분해합
https://www.acmicpc.net/problem/2231
1480ms
"""

answer = 0
n = int(input())
for i in range(1, n):
    result = i + sum(list(map(int, str(i))))
    if result == n:
        answer = i
        break
print(answer)

"""
# 5864ms
import sys

sys.setrecursionlimit(10 * 6)


def solution(total, num, level):
    if level <= 0:
        return total
    num -= (10 ** level) * (num // (10 ** level))
    s = num // (10 ** (level - 1))
    return solution(total + s, num, level - 1)


answer = 0
n = int(input())

for i in range(1, n):
    result = solution(i, i, len(str(i)))
    if result == n:
        answer = i
        break
print(answer)
"""
