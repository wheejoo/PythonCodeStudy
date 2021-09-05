from itertools import combinations

def solution(orders, course):
    answer = []
    print(orders)
    total = [{} for i in range(11)]
    for i in range(len(orders)):
        for j in range(len(course)):
            combis = list(combinations(orders[i],course[j]))
            for z in range(len(combis)):
                str_key = ''.join(sorted(combis[z]))
                if str_key in total[j]:
                    total[j][str_key]+=1
                else:
                    total[j][str_key]=1
    final = []
    for j in range(len(course)):
        big = 2
        total[j] = sorted(total[j].items(), key=lambda x: x[1])
        while len(total[j]) > 1:
            if total[j][-1][1] >= big:
                tmp = total[j].pop()
                big = tmp[1]
                final.append(tmp[0])
            else:
                break
    return sorted(final)