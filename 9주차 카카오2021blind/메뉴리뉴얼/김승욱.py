from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        result = []
        for j in orders:
            j = list(j)
            j.sort()
            result.extend(combinations(j, i))
        if not result:
            continue
        count_result = Counter(result)
        maxx = max(2, max(list(count_result.values())))

        for j in count_result.most_common():
            if j[1] == maxx:
                answer.append(''.join(j[0]))
            else:
                break
        answer.sort()
    return answer