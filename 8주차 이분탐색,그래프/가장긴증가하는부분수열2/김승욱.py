# 풀이참고
from bisect import bisect_left

n = int(input())
value = list(map(int, input().split()))

stack = [0] # 비교하기 위해 0 넣어줌

for a in value:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[bisect_left(stack, a)] = a # a가 들어갈 위치에 a를 넣어준다.
        # a가 들어갈 위치랑 a랑 값이 다를 수 있지만 가장 긴 증가하는 부분 수열의 길이를 구하기 때문에 stack안에 값은 별로 상관없다.

print(len(stack)-1) # 0빼야함