"""
순위 검색 https://programmers.co.kr/learn/courses/30/lessons/72412
"""
from itertools import combinations_with_replacement, permutations
from bisect import bisect_left


# 정확성 100, 효율성 0
def solution(info, query):
    answer = []
    data = [dict() for _ in range(4)]

    info = sorted([x.split(" ") for x in info], key=lambda x: int(x[-1]))
    score_list = [int(x[-1]) for x in info]

    for i in range(len(info)):
        for j in range(4):
            if info[i][j] not in data[j]:
                data[j][info[i][j]] = {i}
            else:
                data[j][info[i][j]].add(i)

    for i in range(len(query)):
        qlist = [x for x in query[i].split(" ") if x != "and"]

        score_range = set(
            [x for x in
             (range(bisect_left(score_list, int(qlist[-1])), len(score_list)))])

        search_list = score_range

        for j in range(4):
            if qlist[j] == "-":
                search_list = search_list & score_range
            else:
                search_list = search_list & data[j][qlist[j]]

        answer.append(len(search_list))
    return answer


# 정확성 100, 효율성 100
def solution(info, query):
    answer = []
    data = dict()

    for inf in info:
        cinfo = inf.split(" ")
        for case in cases:
            for c in case:
                temp = ""
                for i in range(4):
                    if c[i] == 1:
                        temp += "-"
                    else:
                        temp += cinfo[i]
                if temp not in data:
                    data[temp] = [int(cinfo[4])]
                else:
                    data[temp].append(int(cinfo[4]))

    for val in data.values():  # 밖에서 sort안하면 효율성 0
        val.sort()

    for i in range(len(query)):
        count = 0
        qlist = [x for x in query[i].split(" ") if x != "and"]
        qkey = "".join(qlist[:-1])
        if qkey in data:
            qval = data[qkey]
            count = len(qval) - bisect_left(qval, int(qlist[-1]))
        answer.append(count)
    return answer


cases = [set(permutations(list(x), 4)) for x in combinations_with_replacement([0, 1], 4)]

print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
