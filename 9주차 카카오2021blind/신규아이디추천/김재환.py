import re
def solution(new_id):
    # 1단계 소문자변환
    new_id = new_id.lower()
    # 2단계 소문자,숫자,-,_,. 제외 전부 제거
    new_id = re.sub('[^a-zA-Z0-9-_.]','',new_id)
    # 3단계 마침표 2개 이상 제거
    new_id = re.sub('[.]+','.', new_id)
    # 4단계 마침표가 처음이나 끝이면 제거
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5단계 빈문자열이면 "a"대입
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계 길이가 16 이상이면 15개 까지 살리기, 이후 마침표가 끝이 위치하면 . 제거
    new_id = new_id[:15]
    if len(new_id)>=1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7단계 길이가 2자 이하면, 마지막 문자를 길이가 3될때까지 반복
    while len(new_id) <=2:
        new_id = new_id+new_id[-1]
    return new_id