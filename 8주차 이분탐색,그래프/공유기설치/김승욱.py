# 답지봐도 이해가 잘안됨

n, c = map(int, input().split())

value = [int(input()) for _ in range(n)]

value.sort()

l = 1 # l은 집 사이의 거리에 최소값
r = value[-1] - value[0] # r은 집 사이의 거리에 최대값
check = 0
while l <= r:
    mid = (l+r) // 2 # 공유기 설치할 집 사이의 거리
    current = value[0] # 현재 집의 위치에 공유기 설치 (맨처음에 무조건 공유기 설치해야하나?)
    count = 1

    for i in range(1, len(value)):
        if value[i] >= current + mid: # 현재 집의 좌표에서 공유기 설치할 거리만큼 떨어져있다면 공유기 설치
            count += 1
            current = value[i]
    
    if count >= c: # 설치 할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치 할 수 있으므로 l = mid + 1
        l = mid + 1
        check = mid
    else:
        r = mid - 1

print(check)


