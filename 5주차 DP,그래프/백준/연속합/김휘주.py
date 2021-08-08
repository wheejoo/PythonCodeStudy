# https://www.acmicpc.net/problem/1912
# from itertools import permutations -- 쓰려다가 실패,,
# 어렵..다..

n = int(input())
l = list(map(int,input().split()))

sum = [l[0]]
for i in range(len(l) - 1):
    sum.append(max(sum[i] + l[i + 1], l[i + 1])) #sum = [-4,3,4,9,15,-20,12,33,32]
print(max(sum))

# 10 -4 3 1 5 6 -35 12 21 -1 -- 12 + 21
# 2 1 -4 3 4 -4 6 5 -5 1 -- 3 4 -4 6 5
