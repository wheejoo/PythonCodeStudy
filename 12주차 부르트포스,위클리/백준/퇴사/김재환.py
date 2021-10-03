N = int(input())

days = [[]]
for i in range(N):
    days.append(list(map(int, input().split())))

max_money = 0


def calc(day, cost):
    global max_money
    # 해당일에 일을 할 수 있는 경우
    if day <= N and day + days[day][0] <= N+1:
        # day 부터 일을 하는 경우
        calc(day+days[day][0], cost+days[day][1])
        # 일을 안하는 경우
        calc(day+1, cost)
    else:  # 일을 할수없는 경우
        # 다음날로 넘어간다
        if day < N:
            calc(day+1, cost)
        if cost > max_money:
            max_money = cost


# 시작 일
for i in range(1, N+1):
    if i + days[i][0] <= N+1:
        calc(i+days[i][0], days[i][1])
print(max_money)
