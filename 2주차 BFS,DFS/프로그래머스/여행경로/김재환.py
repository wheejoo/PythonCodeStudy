def find(start,path,visited,tickets):
    tmp = []
    for i in range(len(tickets)):
        if start == tickets[i][0] and visited[i] == 0:
            tmpvisited = list(visited) 
            tmpvisited[i] = 1
            tmp.append([path+[tickets[i][1]],tmpvisited])
    tmp = sorted(tmp)
    return tmp
from collections import deque

def solution(tickets):
    path = ["ICN"]
    visited = [0 for i in range(len(tickets))]
    q = deque(find("ICN", path, visited, tickets))
    i = 0
    while q and i<len(tickets)-1:
        i+=1
        for _ in range(len(q)):
            tpath, tvisited = q.popleft()
            q+=find(tpath[i], tpath, tvisited, tickets)
    return q[0][0]