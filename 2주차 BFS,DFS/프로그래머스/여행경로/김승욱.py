def solution(tickets):
    routes = {}
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    
    for r in routes:
        routes[r].sort(reverse=True)
    
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())
    path.reverse()
    return path