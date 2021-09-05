# 효율성 시간초과

def solution(info, query):
    answer = []
    for i in query:
        count = 0
        i = i.split()
        i.insert(-1, 'and')
        i = ''.join(i)
        i = i.split('and')
        for j in info:
            j = j.split()
            for a,b in zip(i,j):
                if not b.isalpha():
                    continue
                if a != b:
                    if a == '-':
                        continue
                    else:
                        break
            else:
                if int(i[-1]) <= int(j[-1]):
                    count += 1
        answer.append(count)
    return answer