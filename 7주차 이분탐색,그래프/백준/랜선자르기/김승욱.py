k, n = map(int, input().split())

value = [int(input()) for _ in range(k)]

l = 1
r = max(value)
check = 0
while l <= r:
    answer = 0
    mid = (l+r)//2
    
    for i in value:
        answer += i // mid

    if answer >= n: # 계속 진행해도 check에는 조건에 맞는 가장 큰 값이 담긴다.
        l = mid + 1
        check = mid
    else:
        r = mid - 1 
print(check)