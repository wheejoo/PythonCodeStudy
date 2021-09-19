"""
가사 검색
https://programmers.co.kr/learn/courses/30/lessons/60060
"""
from collections import defaultdict
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    data = defaultdict(list)
    rdata = defaultdict(list)
    for w in words:
        data[len(w)].append(w)
        rdata[len(w)].append(w[::-1])

    # 역시 중복쿼리가 있기때문에 sort는 밖에서~
    for k in data.keys():
        data[k].sort()
        rdata[k].sort()

    for query in queries:
        dlist = data[len(query)]
        if query[0] == "?":
            dlist = rdata[len(query)]
            query = query[::-1]
        firstq = query.replace("?", "a")
        lastq = query.replace("?", "z")
        count = bisect_right(dlist, lastq) - bisect_left(dlist, firstq)
        answer.append(count)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
