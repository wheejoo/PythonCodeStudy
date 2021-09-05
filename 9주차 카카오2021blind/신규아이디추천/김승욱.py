def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    
    # 2
    
    real_id = ''
    for i in new_id:
        if 97 <= ord(i) <= 122 or i == '-' or i == '_' or i =='.' or 48 <= ord(i) <= 57:
            real_id += i
    
    # 3
    real_id = list(real_id)
    for i in range(len(real_id)-1):
        if real_id[i] == '.' and real_id[i+1] == '.':
            real_id[i] = '!'
    real_id = ''.join(real_id).replace('!', '')
    
    real_id = list(real_id)
    # 4
    if len(real_id) >= 2:
        if real_id[0] == '.':
            real_id.pop(0)
        if real_id[-1] == '.':
            real_id.pop()
    else:
        if real_id[0] == '.':
            real_id.pop()
    
    # 5
    if not real_id:
        real_id.append('a')
    
    # 6
    real_id = real_id[0:15]
    if real_id[-1] == '.':
        real_id.pop()
    
    # 7
    while len(real_id) <= 2:
        real_id.append(real_id[-1])
            
    
    return ''.join(real_id)