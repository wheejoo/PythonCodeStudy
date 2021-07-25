"""
텀 프로젝트 https://www.acmicpc.net/problem/9466
78% 에서 메모리 초과, 시간 초과, 런타임 에러 (RecursionError) -> setrecursionlimit 늘리자
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def dfs(fro, index, path):
    global team, visited, data

    if visited[fro] == 1:  # 이미 방문함
        return

    if path[fro] != 0:  # 사이클이 만들어진 경우(==두번째 방문) 팀 생성
        team += index - path[fro]
        return

    path[fro] = index # path에 방문순번을 저장
    to = data[fro - 1]  # fro가 선택한 학생 == to
    dfs(to, index + 1, path)
    visited[fro] = 1  # 방문처리
    return


for _ in range(int(input())):
    team = 0
    n = int(sys.stdin.readline().rstrip())
    visited = [-1 for _ in range(n + 1)]
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, n + 1):
        if visited[i] == -1:
            dfs(i, 0, defaultdict(int))
    print(n - team)
