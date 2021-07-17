def solution(tickets):
    routes = dict()
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse = True) #도착점 역순정렬
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]: #갈 수 있는 항공권이 있으면
            stack.append(routes[top].pop())
        else: #없으면
            path.append(stack.pop())
    return path[::-1] #역순 반환

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))