n = int(input())

value = [list(map(int, input().split())) for _ in range(n)]
maxx = 0
def recursive(index, total):
    global maxx
    if index > n-1:
        maxx = max(maxx, total)
        return

    if index + value[index][0] <= n:
        recursive(index+value[index][0], total + value[index][1])
    recursive(index+1, total)

recursive(0, 0)
print(maxx)