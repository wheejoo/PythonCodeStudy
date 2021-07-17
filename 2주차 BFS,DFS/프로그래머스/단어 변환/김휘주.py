def solution(begin, target, words):
    answer = 0
    s = [begin]
    if target not in words:
        return 0
    while s:
        new_s = []
        for word in s:
            if word == target:
                return answer
            for word_idx in range(len(words)-1,-1,-1):
                n_word = words[word_idx]
                d = sum([x!=y for x,y in zip(word, n_word)])
                # print([(x,y) for x,y in zip(word, n_word)])
                if d == 1:  #단어 비교 -> 한 글자 차이라면
                    new_s.append(words.pop(word_idx))
        # print(new_s)
        s = new_s
        answer += 1
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))