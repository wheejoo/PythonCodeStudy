"""
표 편집
https://programmers.co.kr/learn/courses/30/lessons/81303
리스트의 삽입, 삭제는 시간이 오래 걸린다. -> LinkedList 로 풀어야 한다.
"""
from bisect import bisect_left


# 정확성 100 효율성 0
def solution2(n, k, cmd):
    buff = []
    atable = [i for i in range(n)]
    now = k

    for c in cmd:
        control = c[0]
        if control == "D":
            now += int(c[2:])
            if now >= len(atable):
                now = len(atable) - 1
        elif control == "U":
            now -= int(c[2:])
            if now < 0:
                now = 0
        elif control == "C":
            buff.append(atable[now])
            del atable[now]
            if now >= len(atable):
                now = len(atable) - 1
        elif control == "Z":
            recover = buff[-1]
            del buff[-1]
            recover_id = bisect_left(atable, recover)
            atable.insert(recover_id, recover)
            if recover_id <= now:
                now += 1

    answer = ["X" for _ in range(n)]
    for i in atable:
        answer[i] = "O"
    return "".join(answer)


def solution(n, k, cmd):
    buff = []
    now = k
    data = {0: [n - 1, 1], n - 1: [n - 2, 0]}
    for i in range(1, n - 1):
        data[i] = [i - 1, i + 1]

    for c in cmd:
        control = c[0]
        if control == "D":
            for _ in range(int(c[2:])):
                now = data[now][1]
        elif control == "U":
            for _ in range(int(c[2:])):
                now = data[now][0]
        elif control == "C":
            buff.append((now, data[now]))
            left, right = data[now]
            data[left][1] = right
            data[right][0] = left
            data[now] = None

            if right == 0:
                now = left
            else:
                now = right
        elif control == "Z":
            recover, reval = buff.pop()
            left, right = reval
            data[recover] = reval
            data[left][1] = recover
            data[right][0] = recover

    answer = ["X" for _ in range(n)]
    for d in [i for i in data.values() if i is not None]:
        left, right = d
        answer[left] = "O"
        answer[right] = "O"

    return "".join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
