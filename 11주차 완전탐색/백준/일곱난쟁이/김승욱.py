value = [int(input()) for _ in range(9)]
check = [False] * 9
answer = []
def recursive(n, index, total):
    global answer
    if n == 7:
        demo = []
        if total == 100:
            for i in range(9):
                if check[i]:
                    demo.append(value[i])
            answer = demo
            return

    if index == len(value):
        return

    check[index] = True
    recursive(n+1, index+1 ,total + value[index])

    check[index] = False
    recursive(n, index+1, total)

recursive(0,0,0)
answer.sort()
for i in answer:
    print(i)