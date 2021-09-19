"""
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058
"""
from collections import deque


def divide(data):
    left, right = 0, 0
    for i in range(len(data)):
        if data[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return data[:i + 1], data[i + 1:]


def check(data):
    if data[0] == ")":
        return False

    stack = deque([])
    for i in range(len(data)):
        if data[i] == "(":
            stack.append("(")
        else:
            stack.pop()
    return not stack


def solution(p):
    if not p:
        return ""
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + "".join(["(" if i == ")" else ")" for i in u[1:-1]])


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
