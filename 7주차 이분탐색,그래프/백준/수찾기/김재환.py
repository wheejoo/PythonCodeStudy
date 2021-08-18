n = int(input())
nl = sorted(list(map(int, input().split())))

n2 = int(input())
n2l = list(map(int, input().split()))

def find(val):
    L = 0
    R = n-1
    while L <= R:
        M = int((L+R)/2)
        if nl[M] == val:
            return 1
        elif nl[M] < val:
            L = M+1
        else:
            R = M-1
    return 0


for i in n2l:
    print(find(i))