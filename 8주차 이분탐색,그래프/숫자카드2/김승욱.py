from bisect import bisect_left, bisect_right

n = int(input())
n_value = list(map(int, input().split()))

m = int(input())
m_value = list(map(int, input().split()))

n_value.sort()
result = []
for i in m_value:
    left = bisect_left(n_value, i)
    right = bisect_right(n_value, i)
    result.append(right - left)

print(*result)