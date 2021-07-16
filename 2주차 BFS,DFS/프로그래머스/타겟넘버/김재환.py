answer = 0

def calc(numbers, i, ret, target):
    global answer
    if i == len(numbers):#종료조건
        if ret == target:
            answer+=1
    else:
        calc(numbers, i+1, ret+numbers[i], target)        
        calc(numbers, i+1, ret-numbers[i], target)    
def solution(numbers, target):
    calc(numbers,0, 0, target)
    return answer