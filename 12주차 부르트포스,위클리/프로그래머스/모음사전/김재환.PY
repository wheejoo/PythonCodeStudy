words= ['A','E','I','O','U']

tmp = []
def DFS(nlist):
    tmp.append(nlist)
    if len(nlist) == 5:
        return 
    for i in words:
        DFS(nlist+[i])
    
def solution(word):
    answer = 0
    total = []
    for n in words:
        DFS([n])
        
    for i in range(len(tmp)):
        if "".join(tmp[i]) == word:
            return i+1
