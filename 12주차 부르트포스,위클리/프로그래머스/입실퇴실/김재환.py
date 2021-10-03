def solution(enter, leave):
    answer = []
    e = 0
    l = 0
    hall = []
    encounter = [0 for i in range(len(enter)+1)]
    # leave를 기준으로 루프 돌기
    while l != len(leave):
        if leave[l] not in hall:
            # 원래 있는 애들은 1씩 증가
            for i in hall:
                encounter[i] += 1
            # 새롭게 들어오는 애는 hall의 인원만큼 증가
            encounter[enter[e]] = len(hall)
            hall.append(enter[e])
            e += 1
        else:
            hall.remove(leave[l])
            l += 1

    return encounter[1:]
