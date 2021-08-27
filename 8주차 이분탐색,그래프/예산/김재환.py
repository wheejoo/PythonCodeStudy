N = int(input())
money = list(map(int, input().split()))
maxi = int(input())

L=0
R=maxi
F = 0
while L<=R:
    M = (L+R)//2
    tmp = []
    for i in range(N):
        if money[i] < M:
            tmp.append(money[i])
        else:
            tmp.append(M)
    if sum(tmp) <= maxi:#적절하다. 좀더 M을 높인다.
        L = M+1
        F = tmp
    else:
        R = M-1
print(max(F))