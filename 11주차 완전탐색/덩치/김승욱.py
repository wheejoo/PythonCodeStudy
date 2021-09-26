n = int(input())

value = [input().split() for _ in range(n)]
answer = []

for i in range(len(value)):
    count = 1
    for j in range(len(value)):
        if value[i][0] < value[j][0]:
            if value[i][1] < value[j][1]:
                count += 1
    answer.append(count)

print(*answer)