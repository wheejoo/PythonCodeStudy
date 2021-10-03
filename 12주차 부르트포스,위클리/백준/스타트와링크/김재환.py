from itertools import combinations
N = int(input())
Tmp = []
for _ in range(N):
    Tmp.append(list(map(int, input().split())))

# 조합구하기
com = list(combinations([i for i in range(N)], N//2))

small = 200000
for i in range(len(com)//2):
    start = list(combinations(com[i], 2))
    link = list(combinations(com[len(com)-1-i], 2))
    start_sum = 0
    link_sum = 0
    for j in range(len(start)):
        a = start[j][0]
        b = start[j][1]
        start_sum += Tmp[a][b] + Tmp[b][a]
        a = link[j][0]
        b = link[j][1]
        link_sum += Tmp[a][b] + Tmp[b][a]
    if small > abs(start_sum - link_sum):
        small = abs(start_sum - link_sum)
print(small)
