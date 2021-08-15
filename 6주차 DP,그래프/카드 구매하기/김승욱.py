n = int(input())

card = [0]+list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = card[1]
dp[2] = max(card[1] * 2, card[2])
for i in range(3, n+1):
    dp[i] = card[i] # 현재 값으로 살수 있는 것과 그전에 값으로 조합해서 살수 있는 것중에 큰것을 저장한다.
    for j in range(1, i//2+1): # i = 6 일 때 j는 6에 반만 돌면 된다.
                                # 1 + 5, 2 + 4, 3 + 3 여기까지만 돌면됨 4 + 2 해도 똑같은 값이 이전에 돌아서 의미없다.
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(max(card))