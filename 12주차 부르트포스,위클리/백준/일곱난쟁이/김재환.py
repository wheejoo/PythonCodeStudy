from itertools import combinations
nan = []
for i in range(9):
    nan.append(int(input()))

com = list(combinations(nan, 7))

for i in range(len(com)):
    if 100 == sum(com[i]):
        for j in sorted(com[i]):
            print(j)
        break
