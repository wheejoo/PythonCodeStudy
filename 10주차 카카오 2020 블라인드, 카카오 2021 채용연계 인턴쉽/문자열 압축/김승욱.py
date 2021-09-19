import sys
def solution(s):
    answer = ''
    result = []
    minn = sys.maxsize
    for i in range(1, len(s)//2+2): # +2 해주는 이유는 문자열 길이가 1일경우 for문이 실행이 안되기 때문에 +2 해준다.
        demo = []
        count = 1
        for j in range(i,len(s)+i,i):
            if s[j:j+i] == s[j-i:j+i-i]:
                count += 1
            else:
                if count >= 2:
                    demo.append(str(count) + s[j-i:j+i-i])
                    count = 1
                else:
                    demo.append(s[j-i:j+i-i])
                    count = 1
        result.append(demo)
    
    for i in result:
        str_result = ''.join(i)
        minn = min(minn, len(str_result))
        
    return minn