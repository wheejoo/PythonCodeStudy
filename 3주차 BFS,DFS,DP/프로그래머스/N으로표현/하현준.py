"""
N으로 표현 https://programmers.co.kr/learn/courses/30/lessons/42895
보고 품 : https://moondol-ai.tistory.com/272
"""


def solution(N, number):
    answer = -1
    dp = [[]]
    for i in range(1, 9):
        data = set()
        data.add(int(str(N) * i))
        for j in range(1, i):
            for k in dp[j]:
                for m in dp[i - j]:
                    data.add(m + k)
                    data.add(abs(m - k))
                    data.add(m * k)
                    if min(m, k) != 0:
                        data.add(max(m, k) // min(m, k))
        if number in data:
            return i
        dp.append(list(data))

    return answer


print(solution(5, 12))
print(solution(2, 11))
