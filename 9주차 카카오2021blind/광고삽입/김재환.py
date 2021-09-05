"""
https://programmers.co.kr/questions/16342
로직은 똑같은데 이거 왜 안되지.....
구간합이니까 투포인터는 맞는거 같은데....
그렇다고 이분탐색은 아니고
단순히 배열을 다 놓고 푸는 문제는 아닌거 같음.

"""

def time_sec_log(time):
    start, end = time.split('-')
    start = time_sec(start)
    end = time_sec(end)
    return start, end

def time_sec(time):
    h,m,s = time.split(':')
    time = int(h)*60*60 + int(m)*60 + int(s)
    return time
def sec_time(sec):
    h = str(sec//(60*60))
    sec = sec%(60*60)
    m = str(sec//60)
    sec = str(sec%60)
    time = ":".join([h.zfill(2),m.zfill(2),sec.zfill(2)])
    return time
    
    
def solution(play_time, adv_time, logs):
    end_time = time_sec(play_time)
    point = [0 for i in range(end_time)]# 구간합 -> 투포인터
    for time in logs:
        start,end = time_sec_log(time)
        for i in range(start, end):
            point[i] += 1
    # 투 포인터
    adtime = time_sec(adv_time)
    total = 0
    # 뒤에서부터로 생각함.
    for i in range(end_time- adtime, end_time):
        total += point[i]
    li = end_time - adtime
    ri = end_time
    big = total
    start_time = 0
    while 0<li:
        li-=1
        total+= point[li]
        ri-=1
        total-= point[ri]
        if total >= big:
            big = total
            start_time = li
    
    return sec_time(start_time)