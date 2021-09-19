def rotation(key):
    ret = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            ret[j][len(key) -1 -i] = key[i][j]
    return ret
        
def check(arr, key, lock):
    for i in range(len(key)-1, len(key) + len(lock)-1):
        for j in range(len(key)-1, len(key) + len(lock)-1):
            if arr[i][j] != 1:
                return False
    return True
    
def reset(key, lock):
    leng = len(key) * 2 + len(lock) - 2
    arr = [[0] * leng for _ in range(leng)]
    for a in range(len(lock)):
        for b in range(len(lock)):
            arr[a + len(key) -1][b + len(key) -1] = lock[a][b]
    return arr

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    
    for i in range(key_len + lock_len -1):
        for j in range(key_len + lock_len -1):
            for k in range(4):
                arr = reset(key, lock)
                key = rotation(key)
                for x in range(key_len):
                    for y in range(key_len):
                        arr[x+i][y+j] += key[x][y]
                chk = check(arr, key, lock)
                if chk:
                    return True
    return False