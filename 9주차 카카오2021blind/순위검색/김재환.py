"""
이상하게 sorted하는 시점에 따라 시간 복잡도가 결정됨.
필요할때만 sorted하는 경우 값이 더 오래 걸린다.
"""
def find(scorelist, target):
    L = 0
    R = len(scorelist)-1
    F = -1
    while L<=R:
        M = (L+R)//2
        if scorelist[M] >= target:
            F = M
            R = M-1
        else:
            L = M+1
    if F == -1: #선택된게 없음
        return 0
    else:
        return len(scorelist) - F

def BFS(final, tmp, orilist, index): #조합 만들기
    if index == 4:
        final.append(tmp)
        return    
    tmp.append(orilist[index])
    BFS(final, list(tmp), orilist,index+1)
    tmp.pop()
    tmp.append('-')
    BFS(final, list(tmp), orilist,index+1)

    
from bisect import bisect_left
def solution(info, query):
    answer = []
    infoMap = {'-':0,'java':1, 'python':2, 'cpp':3, 
                'backend':1, 'frontend':2,
                'junior':1, 'senior':2,
                'pizza':1, 'chicken':2}
    Map = {}
    # 데이터를 hash화해준다.
    for i in range(len(info)):
        tmp = info[i].split()
        final = []
        BFS(final, [], tmp, 0)
        for f in final:
            key = "".join(f)
            if key in Map:
                Map[key].append(int(tmp[-1]))
            else:
                Map[key] = [int(tmp[-1])]
    for key in Map.keys():
        Map[key] = sorted(Map[key])
    count =[]
    # 키에 맞춰 접근해본다.
    for i in range(len(query)):
        tmp = query[i].replace(' and ', ' ').split()
        # 점수 배열 뽑기
        if "".join(tmp[:-1]) in Map:
            scorelist = Map["".join(tmp[:-1])]
        else:
            scorelist= []
        #index = bisect_left(scorelist, int(tmp[-1]))
        #count.append(len(scorelist) - index)
        count.append(find(scorelist, int(tmp[-1])))
    return count

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))

"""
이분탐색까지 써가면서 줄였는데 안됨.
def find(Alist, Blist):
    if len(Alist) <= len(Blist):
        T = Blist
        C = Alist
    else:
        T = Alist
        C = Blist
        
    final = []
    for i in range(len(C)):
        L = 0
        R = len(T)-1
        while L <= R:
            M = (L+R)//2
            if T[M] == C[i]:
                final.append(T[M])
                break
            elif T[M] < C[i]:
                L = M+1
            else:
                R = M-1
    return sorted(final)

def solution(info, query):
    answer = []
    
    hash={}
    # 데이터를 hash화해준다.
    for i in range(len(info)):
        tmp = info[i].split()
        for j in range(4):
            if tmp[j] in hash:
                hash[tmp[j]].append(i)
            else:
                hash[tmp[j]] = [i]    
    # 본격적으로 찾기 시작
    result = []
    for i in range(len(query)):
        tmp = query[i].replace(' and ',' ').split()
        target = [i for i in range(len(info))]
        for j in range(len(tmp)-1):
            if tmp[j] == '-':
                continue
            target = find(target, hash[tmp[j]])
        # 점수 비교
        score = tmp[-1] # 점수
        people = 0
        for z in target:
            info_score = info[z].split()[-1]
            if int(score) <= int(info_score):
                people += 1
        result.append(people)            
    
    return result
"""