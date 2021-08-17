def solution(n, times):
    # 성립해야할 규칙은 sortd된수
    # 우선 sorted
    times = sorted(times)
    L = 1
    R = times[-1]*n
    final = 0
    while R >= L:
        M = int((L+R)/2)
        tmp = 0
        for div in times:
            tmp += int(M / div)
        print(tmp, L,M,R)
        if tmp >= n: # 일단 성립하니 저장하고 낮은거 찾으러간다.
            final = M
            R = M-1
        else: # 안되니까 L을 이동
            L = M+1
    return final