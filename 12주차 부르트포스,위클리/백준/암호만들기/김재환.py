"""
최소 한개의 모음(a,e,i,o,u), 최소 2개의 자음
"""
from itertools import combinations
L, C = map(int, input().split())
tmp = input().split()
mo = []
ja = []
for i in tmp:
    if i in ['a', 'e', 'i', 'o', 'u']:
        mo.append(i)
    else:
        ja.append(i)

s = set()
for i in range(1, len(mo)+1):
    if L - i < 2:  # 최소 자음이 2개가 안되면 연산 불필요
        break
    # mo 조합
    mo_com = list(combinations(mo, i))
    # ja 조합
    ja_com = list(combinations(ja, L-i))

    for j in range(len(mo_com)):
        for z in range(len(ja_com)):
            # 두개 합치기
            tmpL = sorted(mo_com[j]+ja_com[z])
            s.add("".join(tmpL))
for i in sorted(s):
    print(i)
