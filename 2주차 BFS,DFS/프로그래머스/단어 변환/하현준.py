"""
단어 변환 https://programmers.co.kr/learn/courses/30/lessons/43163
dfs ?
"""
from collections import deque


def check(astring, bstring):
    count = 0
    if len(astring) != len(bstring):
        return False

    for i in range(len(astring)):
        for j in range(len(bstring)):
            if i == j and astring[i] == bstring[j]:
                count += 1

    return count == len(astring) - 1


def dfs(begin, target, words):
    q = deque([(begin, [], 0)])
    result = []
    while q:
        case, visited, count = q.pop()

        if target == case:
            result.append(count)
            continue

        wlist = []

        for word in words:
            if word in visited:
                continue
            if check(case, word):
                wlist.append(word)

        if wlist:
            for w in wlist:
                q.append((w, visited + wlist, count + 1))

    return result


def solution(begin, target, words):
    data = dfs(begin, target, words)
    if data:
        return min(data)
    else:
        return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
