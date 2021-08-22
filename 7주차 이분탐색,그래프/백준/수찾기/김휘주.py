# https://www.acmicpc.net/problem/1920
# 참고 - 이분탐색 알고리즘
# 존재하면 1, 존재x 0

n = int(input())
nlist = list(map(int,input().split()))
s_nlist = sorted(nlist)
m = int(input())
mlist = list(map(int,input().split()))

def binary_search(i, s_nlist, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == s_nlist[mid]:
        return 1
    elif i < s_nlist[mid]:
        return binary_search(i, s_nlist, start, mid-1)
    else:
        return binary_search(i, s_nlist, mid+1, end)

for i in mlist: #mlist에 들어있는 수가 nlist에 들어있는지 파악하려고
    start = 0
    end = len(s_nlist)-1
    print(binary_search(i, s_nlist, start, end))