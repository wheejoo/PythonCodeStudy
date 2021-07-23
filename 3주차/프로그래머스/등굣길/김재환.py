def solution(m, n, puddles):#오른쪽이랑 아랫쪽으로만 움직이기
    dp = [[0 for i in range(m)] for i in range(n)]
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    dp[0][0] = 1
    dy = [0,-1] #왼쪽 위쪽
    dx = [-1,0]
    for y in range(n):
        for x in range(m):
            if dp[y][x] == -1:
                continue
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if(0<=ny<n) and (0<=nx<m) and dp[ny][nx] != -1:#웅덩이 아니면 가져온다.
                    dp[y][x] += dp[ny][nx]
    return dp[n-1][m-1]%1000000007