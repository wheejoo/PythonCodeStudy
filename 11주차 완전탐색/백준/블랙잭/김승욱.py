n, m = map(int, input().split())

value = list(map(int, input().split()))
maxx = 0
def recursive(n, index, total):

    global maxx

    if n == 3:
        if total <= m:
           maxx = max(maxx, total)
        return
    
    if index == len(value):
        return

    recursive(n+1, index+1, total+value[index])
    recursive(n, index+1, total)

recursive(0,0,0)
print(maxx)