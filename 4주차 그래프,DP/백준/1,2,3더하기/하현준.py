"""
1, 2, 3 더하기 https://www.acmicpc.net/problem/9095
"""
import sys

sys.setrecursionlimit(60000)


def dfs(start):
    global count
    if start == 0:
        count += 1
        return
    elif start < 0:
        return
    for i in range(1, 4):
        dfs(start - i)  # 현재 상태에서 -1,-2,-3을 한다


for _ in range(int(input())):
    n = int(input())
    count = 0
    dfs(n)
    print(count)
count = 0
