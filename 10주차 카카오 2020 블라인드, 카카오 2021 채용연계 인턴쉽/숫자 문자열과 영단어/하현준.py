"""
숫자 문자열과 영단어
https://programmers.co.kr/learn/courses/30/lessons/81301
"""


def solution(s):
    for i in range(10):
        s = s.replace(data[i], str(i))
    return int(s)


data = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
