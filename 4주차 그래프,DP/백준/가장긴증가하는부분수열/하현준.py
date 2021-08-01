"""
가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053
"""
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    temp = 0
    for j in range(i):
        if arr[i] > arr[j]:
            temp = max(temp, dp[j])
    dp[i] = temp + 1

for d in dp:
    print(f"{d:<4}", end=" ")
print()
for a in arr:
    print(f"{a:<4}", end=" ")
print()
print(max(dp))

