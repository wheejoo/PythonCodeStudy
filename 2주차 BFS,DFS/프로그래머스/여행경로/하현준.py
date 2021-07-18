"""
여행경로 https://programmers.co.kr/learn/courses/30/lessons/43164
같은 경로의 항공권이 여러 개 있을 수 있나?
"""
from collections import deque
from copy import deepcopy


def solution(tickets):
    n = len(tickets)
    answer = []
    airline = {}
    visited = {}

    for ticket in tickets:
        a, b = ticket
        if a not in airline:
            airline[a] = []
        airline[a].append(b)
        if a + b not in visited:
            visited[a + b] = 0
        visited[a + b] += 1

    q = deque([('ICN', ['ICN'], visited)])

    while q:
        fro, path, pvisited = q.pop()

        if len(path) > n:
            answer.append(path)
            continue
        if fro in airline:
            for to in airline[fro]:
                if pvisited[fro + to] != 0:
                    ppvisited = deepcopy(pvisited)
                    ppvisited[fro + to] -= 1
                    q.append((to, path + [to], ppvisited))

    answer.sort()
    return answer[0]


# https://programmers.co.kr/questions/18184 (테스트 케이스)
print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))
print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]))
print(solution(
    [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"],
     ["COO", "BOO"]]))
