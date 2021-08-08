"""
연속합 https://www.acmicpc.net/problem/1912
"""
n = int(input())
dp = []
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0] + arr[1], arr[0], arr[1]))
else:
    dp.append(arr[0])
    dp.append(max(arr[0] + arr[1], arr[0], arr[1]))
    for i in range(2, n):
        if arr[i - 1] < 0:  # if arr[i - 1] <= 0 and arr[i] >= 0 (83% 에서 틀림)
            dp.append(max(arr[i] + arr[i - 1] + dp[i - 2], arr[i]))
        else:
            dp.append(arr[i] + dp[i - 1])

    print(max(dp))

print("".join(f"{str(x):<4}" for x in arr))
print("".join(f"{str(x):<4}" for x in dp))

"""
3
-1 -2 1
5
1 -1 1 -1 1
6
-5 1 2 3 -4 5
3
-1 0 -2
5
-1 -1 0 -1 1
"""
