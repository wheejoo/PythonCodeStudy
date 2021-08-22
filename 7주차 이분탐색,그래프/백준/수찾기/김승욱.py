n = int(input())
n_value = list(map(int, input().split()))

m = int(input())
m_value = list(map(int, input().split()))

n_value.sort()


for i in m_value:
    l = 0
    r = len(n_value) - 1
    check = False
    target = i
    while l <= r:
        mid = (l + r) // 2
        if target == n_value[mid]:
            check = True
            break
        elif target > n_value[mid]:
            l = mid + 1
        elif target < n_value[mid]:
            r = mid - 1
    if check:
        print(1)
    else:
        print(0)