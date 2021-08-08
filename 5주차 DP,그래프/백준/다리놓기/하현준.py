"""
다리 놓기 https://www.acmicpc.net/problem/1010
mC(m-n)
pypy3 에서는 math 모듈의 comb 함수가 없다.
"""
import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(math.comb(m, m - n))
