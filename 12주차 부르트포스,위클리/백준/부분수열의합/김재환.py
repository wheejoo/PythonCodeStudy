from itertools import combinations
N, S = map(int, input().split())
tmp = list(map(int, input().split()))
count = 0
for i in range(1, N+1):
    com = list(combinations(tmp, i))
    for j in range(len(com)):
        if sum(com[j]) == S:
            count += 1
print(count)
