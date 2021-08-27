from collections import Counter
N=int(input())
cards = Counter(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(cards[t], end=" ")

"""N=int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

def find(L,R, target):
    while L<=R:
        M = (L+R)//2
        if cards[M]==target:
            return find(L,M-1,target)+find(M+1,R,target) + 1
        elif cards[M]>target:
            R=M-1
        else:
            L=M+1
    return 0    
for t in targets:
    print(find(0,N-1,t), end=" ")   """