N,C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
L=1
R=house[-1]//2
H=0
while L<=R:
    M = (L+R)//2

    install = 1
    install_list = [house[0]]
    for i in range(1,N):
        if (house[i] - install_list[-1] >= M):
            install_list.append(house[i])
            install += 1
    if install >= C:
        H = M
        L = M+1
    else:
        R = M-1
print(H)
