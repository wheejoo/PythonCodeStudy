def solution(table, languages, preference):
    answer = ''
    score = [0,5,4,3,2,1]
    job = []
    result = []
    demo = []
    for i in table:
        i = i.split()
        job.append(i[0])
        total = 0
        for j in range(len(languages)):
            if languages[j] in i:
                idx = i.index(languages[j])
                total += score[idx] * preference[j]
        result.append(total)
    maxx = max(result)
    for i in range(len(result)):
        if result[i] == maxx:
            demo.append(job[i])
    
    demo.sort()
    
    return demo[0]