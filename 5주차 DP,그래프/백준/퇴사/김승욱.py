# 답지봄
n = int(input())
result = []
for i in range(n):
    result.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)] # 0~6 인덱스까지 1~7일에 값이 들어가는데 n+1로 dp를 만드는 이유는 
                            # dp[i] = dp[i+1] 에서 i가 인덱스 6일 경우 인덱스 에러가 나기때문에 n+1로 dp를 만들어준다.

# 뒤에서 부터 dp를 하는 이유는
# dp[i]에 값을 구하기 위해서는
# 첫번째 i번쨰 일을 할때 + i번째 일을 하는데 걸리는 시간후의 이익 => result[i][1] + dp[i + result[i][0]]
# 두번째 i번째 일을 하지 않고 넘어갔을때 => dp[i+1]
# 둘중에 더 큰 값이 dp[i]에 들어오기 때문에 뒤에서 부터 dp를 해줘야 i번째 일을 하는데 걸리는 시간후의 이익을 더해줄 수 있다.
for i in range(n-1, -1, -1):
    if i + result[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(result[i][1] + dp[i + result[i][0]], dp[i+1])

print(dp[0])
