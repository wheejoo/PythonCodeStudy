"""
01타일 https://www.acmicpc.net/problem/1904
i-3     i-2     i-1     i
                _       1
        _       0       0
dp[i] = dp[i-1] + dp[i-2]
피보나치 아님? 근데 왜 시간 초과냐고..
숫자가 커질 수록 덧셈 연산 속도가 느려진다 -> 15746으로 나눈 나머지만 고려하자
"""
n = int(input())
num = 15746
a, b = 1, 2
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(2, n):
        a, b = b % num, (a + b) % num
    print(b)
