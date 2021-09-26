n = int(input())
answer = 0
def check(a):
    total = a

    while a > 0:
        total += a % 10
        a = a // 10

    return total

for i in range(n+1):
    demo = check(i)
    if demo == n:
        answer = i
        break

print(answer)