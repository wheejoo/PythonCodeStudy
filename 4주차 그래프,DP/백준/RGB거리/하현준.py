"""
RGB거리 https://www.acmicpc.net/problem/1149
"""
import sys

sys.setrecursionlimit(60000)
input = sys.stdin.readline


def dfs(house, color):
    global dp, cost
    if dp[house][color] != -1:
        return dp[house][color]

    for case in list({0, 1, 2} - {color}):
        val = cost[house][color] + dfs(house + 1, case)
        if dp[house][color] == -1:
            dp[house][color] = val
        else:
            dp[house][color] = min(dp[house][color], val)
    return dp[house][color]


n = int(input())
cost = [[]]
for _ in range(n):
    cost.append(list(map(int, input().split())))
dp = [[-1 for _ in range(3)] for _ in range(n + 1)]
dp[n] = cost[n]
for i in range(3):
    dfs(1, i)  # i : 0,1,2 => R,G,B
print(min([int(1e9) if i == -1 else i for i in dp[1]]))
