from collections import deque

def near(t, words): # 다른게 하나만 있는 경우 뽑아낸다. 즉 []
    total = []
    for b in words:
        tmp = []
        for i in range(len(t)):#타켓의 숫자만큼 확인한다.
            if t[i] != b[i]: #같은게 존재하는 경우
                tmp.append(1)
        if sum(tmp) == 1: #다른게 하나만 있다.
            total.append(b)
        else:
            total.append(0)
    return total

def solution(begin, target, words):
    answer = 0
    words = [begin] + words
    q = deque([begin])
    visited = [0 for i in range(len(words)+1)] # words순서대로 들어감
    while q:
        answer += 1
        for i in range(len(q)):
            t = q.popleft()
            print("t:",t)
            print("visitied:",visited)
            if t == target:
                return answer-1
            visited[words.index(t)] = 1 #visited 표시
            total = near(t, words)
            for j in range(len(total)):
                if visited[j] == 0 and total[j] != 0:# 들르지 않고, 하나 차이나느 ㄴ경우
                    q.append(total[j])
        print(q)
    answer=0
    return answer