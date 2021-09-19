def sol(p):
    u = ""
    count1 = 0
    count2 = 0
    
    for idx, i in enumerate(p):
        if i == '(':
            count1 += 1
            u += '('
        else:
            count2 += 1
            u += ')'
        if count1 == count2:
            break
    v = p[idx+1:]
    return u, v

def chk(p):
    check = 0
    flag = False
    for i in p:
        if i == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            break
    else:
        flag = True # 올바른 괄호문자열이 아니다.
    return flag

def solution(p):
    demo = ''
    if p == '':
        return ''
    u,v = sol(p)
    if chk(u):
        return u + solution(v)
    else:
        demo += '('
        demo += solution(v)
        demo += ')'
        u = u[1:-1]
        u = u.replace('(', 'o')
        u = u.replace(')', '(')
        u = u.replace('o', ')')
        
        return demo + u