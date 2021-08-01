# https://www.acmicpc.net/problem/1003
# 참고 https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj1003/

t = int(input())
cnt0 = [1,0]
cnt1 = [0,1]
for i in range(2,41):
    cnt0.append(cnt0[i-1] + cnt0[i-2])
    cnt1.append(cnt1[i-1] + cnt1[i-2])

for _ in range(t):
    n = int(input())
    print(cnt0[n], cnt1[n])


# 시간초과...
# t = int(input())
# def solution_0(n):
#     if n == 0:
#         return 1
#     elif n < 3:
#         return (n-1)
#     else:
#         return solution_0(n-3) + solution_0(n-2)
#
# def solution_1(n):
#     if n < 2:
#         return n
#     else:
#         return solution_1(n-2) + solution_1(n-1)
#
# for _ in range(t):
#     n = int(input())
#     print(solution_0(n),solution_1(n))

# 0 0
# 1 1
# 2 1,0 f(0)+f(1)
# 3 1,1,0 f(2)+f(1)
# 4 1,1,0,1,0
# 5 1,1,0,1,0,1,1,0
# f(n) = f(n-1)+f(n-2)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#         return fibonacci(n-1) + fibonacci(n-2)