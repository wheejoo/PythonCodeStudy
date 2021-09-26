n = int(input())
count = 0

def check(a):
    lis = list(map(int, str(a)))
    demo = 1001

    for i in range(len(lis)-1):
        if demo == 1001:
            demo = lis[i] - lis[i+1]
        else:
            if demo != lis[i] - lis[i+1]:
                return False
    return True


for i in range(1, n+1):
    if check(i):
        count += 1

print(count)