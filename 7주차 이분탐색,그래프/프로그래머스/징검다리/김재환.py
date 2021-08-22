def solution(distance, rocks, n):
    rocks = sorted(rocks) # 정렬해주기
    rocks_num = len(rocks)
    L = 1
    R = distance
    final = 0
    while L<=R:
        M = int((L+R)/2) # 예상하는 최솟값
        remove = 0
        tmp_rocks = [0]
        for i in range(rocks_num):
            if (rocks[i] - tmp_rocks[-1] >= M) and (distance - rocks[i] >= M):# 다리 놓기 가능
                tmp_rocks.append(rocks[i])
            else: # 다리 못놓음
                remove += 1
        if remove <= n:
            final = M
            L = M+1
        else:
            R = M-1
    return final