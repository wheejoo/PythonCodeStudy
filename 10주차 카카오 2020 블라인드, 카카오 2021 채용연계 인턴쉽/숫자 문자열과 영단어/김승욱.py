def solution(s):
    result = ['zero','one','two','three','four','five','six','seven','eight','nine']
    alp = ''
    answer = []
    for i in s:
        if alp in result:
            answer.append(str(result.index(alp)))
            alp = ''
        if i.isalpha():
            alp += i
        else:
            answer.append(i)
        print(alp)
        
    if alp in result:
            answer.append(str(result.index(alp)))
            alp = ''
        
    answer = ''.join(answer)
    return int(answer)