n = int(input())
n_value = list(map(int, input().split()))

m = int(input())
m_value = list(map(int, input().split()))

n_value.sort()
result = []
for i in m_value:
    flag = False
    l = 0
    r = len(n_value) -1
    while l <= r:
        mid = (l+r) // 2
        if i == n_value[mid]:
            flag = True
            break

        if i > n_value[mid]:
            l = mid + 1
        else:
            r = mid - 1
    if flag:
        result.append(1)
    else:
        result.append(0)
print(*result)