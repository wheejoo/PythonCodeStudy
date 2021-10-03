N = int(input())

total = 0
for i in range(1, N+1):
    # 자리수가 2이하이면 그냥 더함.
    if i//100 == 0:
        total += 1
        continue
    # 3부터면 각 자리수의 차가 같은지 검증
    d1 = int(str(i)[0]) - int(str(i)[1])
    d2 = int(str(i)[1]) - int(str(i)[2])
    if d1 == d2:
        total += 1
print(total)
