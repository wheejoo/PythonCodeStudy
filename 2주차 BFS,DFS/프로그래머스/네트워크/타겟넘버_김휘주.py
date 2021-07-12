from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    while q:
        n_sum, n_idx = q.popleft()
        if n_idx == len(numbers):
            if n_sum == target:
                answer += 1
        else:
            number = numbers[n_idx]
            q.append((n_sum+number, n_idx+1))
            q.append((n_sum-number, n_idx+1))
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))