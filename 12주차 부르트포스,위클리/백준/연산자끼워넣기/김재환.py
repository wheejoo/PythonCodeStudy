N = int(input())
num = list(map(int, input().split()))
calcs = list(map(int, input().split()))
max_value = -1000000000000
min_value = 1000000000000


def calc(total, order, info):
    global max_value
    global min_value
    if order == N:
        if max_value < total:
            max_value = total
        if min_value > total:
            min_value = total
        return

    # 연산 진행전 info를 확인한다. + - * %
    if info[0] > 0:
        next_info = list(info)
        next_info[0] -= 1
        calc(total+num[order], order+1, next_info)
    if info[1] > 0:
        next_info = list(info)
        next_info[1] -= 1
        calc(total-num[order], order+1, next_info)
    if info[2] > 0:
        next_info = list(info)
        next_info[2] -= 1
        calc(total*num[order], order+1, next_info)
    if info[3] > 0:
        next_info = list(info)
        next_info[3] -= 1
        if total < 0:
            calc(-(abs(total)//num[order]), order+1, next_info)
        else:
            calc(total//num[order], order+1, next_info)


calc(num[0], 1, calcs)
print(max_value)
print(min_value)
