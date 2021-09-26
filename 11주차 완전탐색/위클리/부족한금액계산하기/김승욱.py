def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i

    answer = 0 if answer <= money else answer - money
    return answer