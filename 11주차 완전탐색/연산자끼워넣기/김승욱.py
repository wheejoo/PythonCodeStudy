import sys
n = int(input())
value = list(map(int, input().split()))
op = list(map(int, input().split()))
maxx = -(sys.maxsize)
minn = sys.maxsize
def recursive(index,plus,minus,mul,div, total):

    global maxx, minn
    
    if index == n:
        maxx = max(maxx, total)
        minn = min(minn, total)
        return

    if plus > 0:
        recursive(index+1,plus-1, minus, mul, div, total+value[index])
    if minus > 0:
        recursive(index+1,plus, minus-1, mul, div, total-value[index])
    if mul > 0:
        recursive(index+1,plus, minus, mul-1, div, total*value[index])
    if div > 0:
        if total < 0:
            recursive(index+1,plus, minus, mul, div-1, -(-total//value[index]))
        else:
            recursive(index+1,plus, minus, mul, div-1, total//value[index])

recursive(1,op[0],op[1],op[2],op[3],value[0])
print(maxx)
print(minn)