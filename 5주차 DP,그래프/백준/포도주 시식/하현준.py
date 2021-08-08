"""
포도주 시식 https://www.acmicpc.net/problem/2156
(계단 오르기 https://www.acmicpc.net/problem/2579 와 비슷하네)

i-4     i-3     i-2     i-1     i
        _       0       1       1
                _       0       1
_       0       1       1       0
"""
n = int(input())
data = []
dp = []
for _ in range(n):
    data.append(int(input()))

if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
elif n == 3:
    print(max(data[0] + data[1], data[0] + data[2], data[1] + data[2]))
else:
    dp.append(data[0])
    dp.append(data[0] + data[1])
    dp.append(max(data[0] + data[1], data[0] + data[2], data[1] + data[2]))
    dp.append(max(data[0] + data[1] + data[3], data[0] + data[2] + data[3]))
    for i in range(4, n):
        dp.append(max(data[i] + data[i - 1] + dp[i - 3],
                      data[i] + dp[i - 2],
                      data[i - 1] + data[i - 2] + dp[i - 4],
                      ))
    print(dp[-1])

print("".join(f"{str(x):<4}" for x in data))
print("".join(f"{str(x):<4}" for x in dp))
"""
10
1
11
11
11
1
11
11
11
1
1
"""