n = int(input())
grape = [0] * 10000
for i in range(n):
    grape[i] = int(input())

dp = [0] * 10000
dp[0] = grape[0]
dp[1] = grape[1] + grape[0]
dp[2] = max(grape[2] + grape[0], grape[1] + grape[2], dp[1])

for i in range(3, n):
    dp[i] = max(grape[i] + dp[i-2], grape[i] + grape[i-1] + dp[i-3], dp[i-1])

print(max(dp))

# o o x o => graph[i] + dp[i-2]
# o x o o => graph[i] + graph[i-1] + dp[i-3] (graph[i] + dp[i-1]로 하게되면 연속해서 3개 오는 경우가 있을수 있음)

# o x o x
# o o x x
# x o o x => 현재 위치를 안먹는게 최댓값일 수 있음 ex) 1, 200, 500, 2
# 이러한 경우들은 dp[i-1]에 가장 큰값이 저장되어있다.

