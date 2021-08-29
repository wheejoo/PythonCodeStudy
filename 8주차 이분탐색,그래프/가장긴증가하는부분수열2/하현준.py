"""
가장 긴 증가하는 부분 수열 2 https://www.acmicpc.net/problem/12015
LIS 알고리즘 참고 : https://chanhuiseok.github.io/posts/algo-49/
(feat. 이분탐색)
pypy3 : 616ms
python3 : 3940ms
"""


def search(sdp, target):
    lo = -1
    hi = len(sdp)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        temp = sdp[mid]
        if temp > target:
            hi = mid
        elif temp == target:
            return mid
        else:
            lo = mid
    print(f"{target=} {lo=}")
    return lo + 1


def lis(arr):
    dp = [arr[0]]
    for i in range(len(arr)):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            index = search(dp, arr[i])
            dp[index] = arr[i]
        print(f"{dp=}")
    return len(dp)


n = int(input())
data = list(map(int, input().split()))
print(lis(data))
