"""
이친수 https://www.acmicpc.net/problem/2193
"""
n = int(input())
zdp = [0 for _ in range(n + 1)]
odp = [0 for _ in range(n + 1)]

if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    zdp[1], odp[1] = 0, 1
    zdp[2], odp[2] = 1, 0
    zdp[3], odp[3] = 1, 1

    for i in range(4, n + 1):
        zdp[i] = zdp[i - 1] + zdp[i - 2]
        odp[i] = odp[i - 1] + odp[i - 2]
    print(zdp[n] + odp[n])
