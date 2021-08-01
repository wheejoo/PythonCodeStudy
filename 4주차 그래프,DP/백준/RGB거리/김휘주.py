# https://www.acmicpc.net/problem/1149
# 참고 https://chunghyup.tistory.com/48

n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))
# print(rgb)

def solution(n,rgb):
    for i in range(1, n): #빨 - 초 - 파
        rgb[i][0] = rgb[i][0] + min(rgb[i - 1][1], rgb[i - 1][2])
        rgb[i][1] = rgb[i][1] + min(rgb[i - 1][0], rgb[i - 1][2])
        rgb[i][2] = rgb[i][2] + min(rgb[i - 1][0], rgb[i - 1][1])
    return min(rgb[n - 1][0], rgb[n - 1][1], rgb[n - 1][2])

print(solution(n,rgb))