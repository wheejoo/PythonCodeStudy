"""
설탕 배달 https://www.acmicpc.net/problem/2839
dp를 쓰게 된다면 N=5000일 때, 메모리 낭비 큼
답안 참고
"""

n = int(input())
bag = 0
while True:
    if n % 5 == 0:
        bag += n // 5  # n//5의 의미 = 5kg 봉투 개수
        print(bag)
        break
    n -= 3
    bag += 1  # bag +1하는 이유 = 3kg 봉투 1개 추가하기 때문
    if n < 0:
        print(-1)
        break
