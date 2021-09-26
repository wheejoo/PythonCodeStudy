"""
덩치
https://www.acmicpc.net/problem/7568
"""
answer = []
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    count = 1
    for j in range(n):
        if i != j:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                count += 1
    answer.append(count)

print(" ".join(list(map(str, answer))))
