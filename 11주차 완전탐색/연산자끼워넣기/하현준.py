"""
연산자 끼워넣기
https://www.acmicpc.net/problem/14888
python3 104ms
"""
import sys


def dfs(i, res, add, sub, mul, div):
    global vmin, vmax
    if i == n:
        vmax = max(vmax, res)
        vmin = min(vmin, res)
        return
    if add > 0:
        dfs(i + 1, res + nums[i], add - 1, sub, mul, div)
    if sub > 0:
        dfs(i + 1, res - nums[i], add, sub - 1, mul, div)
    if mul > 0:
        dfs(i + 1, res * nums[i], add, sub, mul - 1, div)
    if div > 0:
        dfs(i + 1, int(res / nums[i]), add, sub, mul, div - 1)


sys.setrecursionlimit(10 ** 6)
answer = []
n = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))

vmin, vmax = float('inf'), -float('inf')

dfs(1, nums[0], temp[0], temp[1], temp[2], temp[3])
print(vmax)
print(vmin)

"""
python3 시간초과
pypy3 2652ms

from itertools import permutations

answer = []
n = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))

oper = []
for i in range(4):
    oper.extend([i for _ in range(temp[i])])

cases = list(permutations(oper, n - 1))

for case in cases:
    result = nums[0]
    for i in range(n - 1):
        if case[i] == 0:
            result += nums[i + 1]
        elif case[i] == 1:
            result -= nums[i + 1]
        elif case[i] == 2:
            result *= nums[i + 1]
        elif case[i] == 3:
            ctemp = abs(result)
            ctemp //= nums[i + 1]
            result = -ctemp if result < 0 else ctemp
    answer.append(result)

print(max(answer))
print(min(answer))
"""
