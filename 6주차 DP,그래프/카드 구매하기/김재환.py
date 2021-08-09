n = int(input())
p = [0]+list(map(int, input().split()))

for i in range(2, n+1):
    big = p[i]
    for k in range(i-1,int(i/2)-1, -1):
        if p[k]+p[i-k] > big:
            big = p[k]+p[i-k]
    p[i] = big
print(p[n])
