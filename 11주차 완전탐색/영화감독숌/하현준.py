"""
영화감독 숌
https://www.acmicpc.net/problem/1436
"""
n = int(input())

i = 0
cnt = 0
answer = 0
while True:
    i += 1
    if str(i).count("666") > 0:
        cnt += 1
        answer = i

    if cnt == n:
        break

print(answer)

"""
100666 ~ 105666 (6)
    106660 ~ 106669 (10)
107666 ~ 109666 (3)

110666 ~ 115666
    116660 ~ 116669
117666 ~ 119666
..

160666 ~ 165666 (6)
    166660 ~ 166699 (40)
167666 ~ 169666 (3)
"""
