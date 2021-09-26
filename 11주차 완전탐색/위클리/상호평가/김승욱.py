def solution(scores):
    answer = ''
    avg = []
    for i in range(len(scores[0])):
        demo = []
        for j in range(len(scores)):
            demo.append(scores[j][i])
        maxx = max(demo)
        minn = min(demo)
        if demo.count(maxx) == 1:
            if demo.index(maxx) == i:
                demo.remove(maxx)
                
        if demo.count(minn) == 1:
            if demo.index(minn) == i:
                demo.remove(minn)
                
        avg.append(sum(demo) / len(demo))
    
    for i in avg:
        if i >= 90:
            answer += 'A'
        elif i >= 80:
            answer += 'B'
        elif i >= 70:
            answer += 'C'
        elif i >= 50:
            answer += 'D'
        else:
            answer += 'F'
            
    return answer