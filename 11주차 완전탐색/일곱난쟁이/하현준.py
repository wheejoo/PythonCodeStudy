"""
일곱 난쟁이
https://www.acmicpc.net/problem/2309
"""
from itertools import combinations

answer = []
cases = list(combinations([int(input()) for _ in range(9)], 7))
for case in cases:
    if sum(case) == 100:
        answer.append(sorted(case))

print("\n".join(list(map(str, answer[0]))))
