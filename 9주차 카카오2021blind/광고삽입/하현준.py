"""
광고 삽입 https://programmers.co.kr/learn/courses/30/lessons/72414
참고 : https://0equal2.tistory.com/70
"""


def decode_time(dstring):
    dlist = [int(x) for x in dstring.split(":")]
    return dlist[0] * 3600 + dlist[1] * 60 + dlist[2]


def encode_time(eint):
    h = eint // 3600
    m = (eint - 3600 * h) // 60
    s = eint - 3600 * h - 60 * m
    return f"{h:02}:{m:02}:{s:02}"


def solution(play_time, adv_time, logs):
    play_time, adv_time = decode_time(play_time), decode_time(adv_time)
    cumulate = [0 for _ in range(play_time + 1)]

    for log in logs:
        st, et = log.split("-")
        st, et = decode_time(st), decode_time(et)
        cumulate[st] += 1
        cumulate[et] -= 1

    for _ in range(2):
        for i in range(1, play_time + 1):
            cumulate[i] += cumulate[i - 1]

    start_time = 0
    max_play = cumulate[adv_time - 1]

    for i in range(adv_time, play_time):
        play = cumulate[i] - cumulate[i - adv_time]
        if max_play < play:
            max_play = play
            start_time = i - adv_time + 1

    return encode_time(start_time)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
