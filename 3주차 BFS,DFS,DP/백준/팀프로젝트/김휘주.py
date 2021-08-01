# https://www.acmicpc.net/problem/9466
##참고
# https://velog.io/@zwooo96/%EB%B0%B1%EC%A4%80-9466%EB%B2%88-%ED%85%80-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

def dfs(v):
    global cnt
    visited[v] = True
    team.append(v) #팀에 추가

    if num[v] == v: #자기자신 선택
        team.pop() #pop

    if not visited[num[v]]: #방문x
        dfs(num[v])
    else:
        if team: #만들어진 팀o
            temp = 0
            for j in range(len(team)):
                if team[j] != num[i]: #순환하는가
                    temp += 1
                else:
                    cnt += temp #순환에 속하지 않는 학생 추가
                return
            cnt += len(team) #팀에 속하지 않은 학생 추가
        return

t = int(input())
for _ in range(t):
    n = int(input())
    num = [0] + list(map(int,input().split())) #인덱스 붙여주기
    visited = (False) * (n+1)
    cnt = 0
    for i in range(n):
        team = []
        if not visited[i]:
            dfs(i)
    print(cnt)