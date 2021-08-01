"""
순위 https://programmers.co.kr/learn/courses/30/lessons/49191
플로이드 워샬 (참고)
"""


def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for a in range(1, n + 1):
        lose, win = 0, 0
        for b in range(1, n + 1):
            if graph[a][b] != 0 and graph[a][b] != INF:
                win += 1
            if graph[b][a] != 0 and graph[b][a] != INF:
                lose += 1
        # a선수 보다 강한 선수들 = lose
        # a선수 보다 약한 선수들 = win
        if lose + win == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
