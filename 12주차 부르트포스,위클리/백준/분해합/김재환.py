N = int(input())

small = 0
for i in range(0, N):
    tmp = 0
    nlist = list(map(int, str(i)))
    tmp += i + sum(nlist)
    if tmp == N:
        small = i
        break
if small == 0:
    print(0)
else:
    print(small)
