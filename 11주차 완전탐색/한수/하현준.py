"""
한수
https://www.acmicpc.net/problem/1065
"""
answer = 0
n = int(input())
for i in range(1, n + 1):
    tlist = list(map(int, str(i)))
    if len(tlist) == 1:
        answer += 1
    else:
        check = True
        old_term = tlist[1] - tlist[0]
        for j in range(1, len(tlist) - 1):
            new_term = tlist[j + 1] - tlist[j]
            if old_term != new_term:
                check = False
                break
        if check:
            answer += 1
print(answer)
