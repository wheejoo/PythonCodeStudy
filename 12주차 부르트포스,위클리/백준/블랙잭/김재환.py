from itertools import combinations
N, M = map(int, input().split())
num = list(map(int, input().split()))

com = list(combinations(num, 3))

big = 0
for i in com:
    if big < sum(i) <= M:
        big = sum(i)
print(big)
