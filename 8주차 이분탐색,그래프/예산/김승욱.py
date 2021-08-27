n = int(input())
value = list(map(int, input().split()))
money = int(input())

l = 1
r = max(value)
check = 0
while l <= r:
    answer = 0
    mid = (l + r) // 2

    for i in value:
        if i >= mid: # 상한액 보다 큰 경우
            answer += mid # 상한액만 더해준다.
        else:
            answer += i # 상한액보다 작은 경우 원래값 더해준다.
    
    if answer > money: # 총합이 예산보다 큰 경우
        r = mid - 1 # 상한액을 줄여야함
        
    else: # 총합이 예산보다 작거나 같은 경우
        l = mid + 1 # 상한액을 올려준다.
        check = mid # answer > money 쪽에 넣었다가 안돼서 옮겼는데 헷갈린다.
print(check)