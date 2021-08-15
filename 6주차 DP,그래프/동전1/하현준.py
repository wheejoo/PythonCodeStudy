"""
동전1 https://www.acmicpc.net/problem/2293
모르겠다.. 참고 -> https://debuglog.tistory.com/78
        k   0   1   2   3   4   5   6   7   8   9   10
c(0)    [0] 1   0   0   0   0   0   0   0   0   0   0
c(1)    [1] 1   1   1   1   1   1   1   1   1   1   1
c(2)    [2] 1   1   2   2   3   3   4   4   5   5   6
c(3)    [5] 1   1   2   2   3   4   5   6   7   8   10
빡통대가리는 노력하자
"""
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count_list = [0] * (k + 1)
count_list[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        count_list[i] += count_list[i - coin]
    print(coin, count_list)

print(count_list[k])
