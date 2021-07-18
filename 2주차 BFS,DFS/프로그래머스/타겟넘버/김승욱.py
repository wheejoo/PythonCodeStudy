def solution(numbers, target):
    answer = 0
    def dfs(index, result):
        nonlocal answer
        if index == len(numbers):
            if result == target:
                answer += 1
            return
        else:
            dfs(index + 1, result + numbers[index])
            dfs(index + 1, result - numbers[index])
    dfs(0,0)
    return answer