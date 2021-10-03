N = int(input())
dung = []
for _ in range(N):
    dung.append(list(map(int, input().split())))

score = [1 for i in range(N)]
for i in range(N):
    t1 = dung[i]
    for j in range(i+1, N):
        t2 = dung[j]

        if t1[0] > t2[0] and t1[1] > t2[1]:
            score[j] += 1
        if t1[0] < t2[0] and t1[1] < t2[1]:
            score[i] += 1
for i in score:
    print(i, end=" ")
