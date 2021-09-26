"""
블랙잭
https://www.acmicpc.net/problem/2798
"""
answer = 0
n, m = map(int, input().split())
card = sorted(list(map(int, input().split())), reverse=True)
for i in range(n - 2):
    count = 1
    total = card[i]
    if total < m:
        for j in range(i + 1, n - 1):
            if total + card[j] < m:
                count += 1
                total += card[j]
                for k in range(j + 1, n):
                    if total + card[k] <= m:
                        count += 1
                        total += card[k]
                        answer = max(answer, total)
                        count -= 1
                        total -= card[k]
            count -= 1
            total -= card[j]
    count -= 1
    total -= card[i]

print(answer)
