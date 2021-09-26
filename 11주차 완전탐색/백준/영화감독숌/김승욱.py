n = int(input())

value = []
i = 0
while len(value) < 10000:
    if '666' in str(i):
        value.append(i)
    i += 1


print(value[n-1])