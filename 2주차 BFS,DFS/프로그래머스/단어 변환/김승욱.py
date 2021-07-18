def solution(begin, target, words):
    answer = 0
    result = []
    if target not in words:
        return 0
    elif target == begin:
        return 0
    visited = [False] * len(words)
    
    
    def dfs(begin, target, words, visited, answer):
        nonlocal result
        if begin == target:
            return result.append(answer)
        change = []
        
        for word in words:
            count = 0
            for i in range(len(word)):
                if begin[i] != word[i]:
                    count += 1
            if count == 1:
                change.append(word)
        
        for word in change:
            if visited[words.index(word)] == False:
                visited[words.index(word)] = True
                dfs(word, target, words, visited, answer + 1)
                visited[words.index(word)] = False
                
    dfs(begin, target, words, visited, answer)
    return min(result)