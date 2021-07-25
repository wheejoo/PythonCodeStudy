def solution(N, number):
    answer = -1
    DP = [None] + [{int(str(N) * i)} for i in range(1,9)]
    for i in range(1, 9):
        for j in range(1, i):
            for x in DP[j]:
                # DP[4]를 만들기 위해서는 
                # DP[1] + DP[3]
                # DP[2] + DP[2]
                # DP[2] + DP[2]
                # DP[3] + DP[1] 를 다돌아준다. 반까지만 돌고 y - x와 y // x를 추가하는 방법도 있다.
                for y in DP[i-j]:
                    DP[i].add(x + y)
                    DP[i].add(x - y)
                    DP[i].add(x * y)
                    if y:
                        DP[i].add(x//y)
        if number in DP[i]:
            return i
    return answer