# https://www.acmicpc.net/problem/2156
# 참고 https://pacific-ocean.tistory.com/152
# 참고를 했지만,, 어렵,,

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
result = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        result[1] = wine[1]
    elif i == 2:
        result[2] = wine[1] + wine[2]
    else:
        result[i] = max(result[i-3] + wine[i-1] + wine[i], result[i-2] + wine[i], result[i-1])

print(result[i])

# 6
# 6 10 13 9 8 1

