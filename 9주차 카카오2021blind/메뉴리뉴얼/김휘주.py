from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        array = []
        for order in orders:
            order = sorted(order)
            # c개 조합
            array += list(combinations(order, c))

        count = Counter(array)

        if count:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    # 가장 많이시킨거
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)