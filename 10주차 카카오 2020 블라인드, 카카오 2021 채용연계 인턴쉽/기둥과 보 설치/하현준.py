"""
기둥과 보 설치
https://programmers.co.kr/learn/courses/30/lessons/60061
"""


def check(build):
    for bu in build:
        x, y, a = bu
        if a == 0:  # 기둥
            if not (y == 0 or [x, y - 1, 0] in build or [x - 1, y, 1] in build or [x, y, 1] in build):
                return False
        else:  # 보
            if not ([x, y - 1, 0] in build or [x + 1, y - 1, 0] in build or (
                    [x - 1, y, 1] in build and [x + 1, y, 1] in build)):
                return False
    return True


def solution(n, build_frame):
    build = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:  # 삭제
            build.remove([x, y, a])
            if not check(build):
                build.append([x, y, a])
        else:  # 설치
            build.append([x, y, a])
            if not check(build):
                build.remove([x, y, a])
    build.sort()
    return build


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
