n,m = map(int, input().split())
tree = list(map(int, input().split()))

L=1
R=max(tree)
H = 0
while L<=R:
    M = int((L+R)//2)
    tmp=0
    for i in range(n):
        if tree[i] > M:
            tmp += tree[i] - M
            if tmp > m:# 요게 들어가는게 포인트
                break
    if tmp >= m:
        H = M
        L = M+1
    else:
        R = M-1
print(H)