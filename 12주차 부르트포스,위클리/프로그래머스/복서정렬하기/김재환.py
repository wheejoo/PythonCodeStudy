def solution(weights, head2head):
    answer = []
    players = []
    for i in range(len(weights)):
        player = []
        # 승률
        match = 0
        win = 0
        jamu = 0
        for j in range(len(weights)):
            if j == i:
                continue
            if head2head[i][j] == "N":
                continue
            match += 1
            if head2head[i][j] == "W":
                if weights[i] < weights[j]:  # 자무복이
                    jamu += 1
                win += 1
        if match != 0:
            player.append(win/match)
        else:
            player.append(0)
        # 잡무복이
        player.append(jamu)
        # 몸무게
        player.append(weights[i])
        player.append(i+1)
        players.append(player)
    players.sort(key=lambda x: (x[0], x[1], x[2], -x[3]))
    for i in players:
        answer.append(i[3])

    return list(reversed(answer))
