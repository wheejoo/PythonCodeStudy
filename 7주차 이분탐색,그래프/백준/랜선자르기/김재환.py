k,n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

L = 1
R = max(lan)

length = 0
while L<=R:
    M = (L+R)//2
    tmp = 0
    for i in lan:
        tmp += i//M
    if tmp >= n:
        length = M
        L = M+1
    else:
        R = M-1
print(length)