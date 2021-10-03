def check(number):  # 연속 6 3개인지 판별
    S_number = str(number)
    for _ in range(0, len(S_number)-2):
        flag = 0
        for i in range(3):
            if S_number[_+i] == '6':
                flag += 1
            if flag == 3:
                return True
    return False


N = int(input())

i = 666
tmp = 0
while N != 0:
    if check(i):
        N -= 1
        tmp = i
        i += 1
    else:
        i += 1

print(tmp)
