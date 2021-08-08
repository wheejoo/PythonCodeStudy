# https://www.acmicpc.net/problem/1010
# https://yoonsang-it.tistory.com/33 - factoiral 불러서 사용할 수도 있음!
# from itertoosl import combinations - 순열,, 쓰고 싶었는데,, 실패,, 
from math import factorial

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    b = factorial(m) // (factorial(n) * factorial(m-n))
    print(b)


# 2c2 - 2
# 5c1 - 5
# 29c13 - 67863915