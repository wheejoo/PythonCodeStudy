"""
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057
"""


def solution(s):
    if len(s) == 1:
        return 1

    answer = float('inf')
    for unit in range(1, len(s) // 2 + 1):
        uresult = []
        ulist = [s[i:i + unit] for i in range(0, len(s), unit)]

        count = 1
        now = ulist[0]
        for i in range(1, len(ulist) + 1):
            if i == len(ulist):
                count = count if count > 1 else ""
                uresult.append(f"{count}{now}")
            elif now == ulist[i]:
                count += 1
            else:
                count = count if count > 1 else ""
                uresult.append(f"{count}{now}")
                now = ulist[i]
                count = 1
        uresult = "".join(uresult)
        answer = min(answer, len(uresult))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))
