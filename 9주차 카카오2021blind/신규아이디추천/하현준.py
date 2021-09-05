"""
신규 아이디 추천 https://programmers.co.kr/learn/courses/30/lessons/72410
진짜 괴물들 많네
"""


def step12(string):
    ret = ""
    string = string.lower()
    for n in string:
        if n.isalnum() or n == "-" or n == "_" or n == ".":
            ret += n
    return ret


def step3(string):
    ret = ""
    start, end = 0, 0
    dcheck = True
    for i in range(len(string)):
        if string[i] == ".":
            if dcheck:
                ret += string[start:end + 1]
                start = i + 1
                end = i + 1
                dcheck = False
            else:
                start += 1
                end += 1
        else:
            dcheck = True
            end += 1
    ret += string[start:end + 1]
    return ret


def step4(string):
    start, end = 0, len(string)
    if string[0] == ".":
        start += 1
    if string[-1] == ".":
        end -= 1
    return string[start:end]


def step567(string):
    if not string:
        string += "a"
    if len(string) >= 16:
        string = string[:15]
        if string[-1] == ".":
            string = string[:-1]
    if len(string) <= 2:
        s = string[-1]
        while len(string) != 3:
            string += s
    return string


def solution(new_id):
    return step567(step4(step3(step12(new_id))))


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
