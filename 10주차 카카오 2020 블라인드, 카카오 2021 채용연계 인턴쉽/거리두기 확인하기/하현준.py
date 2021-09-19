"""
거리두기 확인하기
https://programmers.co.kr/learn/courses/30/lessons/81302
"""
from itertools import combinations


def man_dist(mdata):
    a, b = mdata
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_near_location(gdata):
    ret = set()
    x, y = gdata
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 5 and 0 <= yy < 5:
            ret.add((xx, yy))
    return ret


def solution(places):
    answer = []
    for place in places:
        check = True
        people = []
        graph = [list(x) for x in place]
        for i in range(5):
            for j in range(5):
                if graph[i][j] == "P":
                    people.append([i, j])
        for case in combinations(people, 2):
            dist = man_dist(case)
            if dist == 1:
                check = False
            elif dist == 2:
                a_location = get_near_location(case[0])
                b_location = get_near_location(case[1])
                for location in a_location & b_location:
                    xx, yy = location
                    if graph[xx][yy] == "O":
                        check = False
        answer.append(1 if check else 0)
    return answer


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

