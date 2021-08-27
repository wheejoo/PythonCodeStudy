from collections import Counter
N=int(input())
cards = Counter(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(cards[t], end=" ")