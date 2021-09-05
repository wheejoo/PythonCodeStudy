"""
메뉴 리뉴얼 https://programmers.co.kr/learn/courses/30/lessons/72411
"""
from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        data = defaultdict(int)
        ocases = [set(combinations(order, c)) for order in orders]
        for i in range(len(ocases) - 1):
            for j in range(i + 1, len(ocases)):
                a = set(["".join(sorted(x)) for x in ocases[i]])
                b = set(["".join(sorted(x)) for x in ocases[j]])
                for it in ["".join(x) for x in a & b]:
                    data[it] += 1
        if data:
            maxval = max(list(data.values()))
            data = [x[0] for x in data.items() if x[1] == maxval]
            answer.extend(data)
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
