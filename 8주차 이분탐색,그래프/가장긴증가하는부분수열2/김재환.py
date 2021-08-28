"""
자꾸 시간초과 나서 LIS 공부후 다시 제출
LIS 어렵다
1. DP방법 N^2
2. 이분 탐색 방법 N logN
"""
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

for val in A:
    if lis[-1] < val:
        lis.append(val)
        continue
    
    # 이분탐색으로 적절한 위치 찾기
    # 더 작은 값으로 바꾸기 위함
    L=0
    R=len(lis)-1
    while L<=R:
        M = (L+R)//2
        if lis[M] < val: # 부적합
            L = M+1
        else:
            R = M-1
    lis[L]=val
print(len(lis))

"""import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B =[]
for i in range(N):
    B.append((A[i],i))
B = sorted(B)
count = 0
L = 0
R = N-1
val = 0
i = -1
while L <= R:
    F = 0 # 최종 최솟값
    while L <= R:
        M = (L+R)//2

        tval,ti = B[M]
        if tval > val and ti > i: #만족
            R = M-1
            F = M
        else:
            L = M+1
    val, i = B[F]
    L = F+1
    R = N-1
    count+=1
print(count)"""