from collections import defaultdict

def solution(tickets):
    tickets.sort(key= lambda ticket: (ticket[0], ticket[1]))

    fromto = defaultdict(list)
    for i, ticket in enumerate(tickets):
        fromto[ticket[0]].append((i, ticket[1]))
    print(fromto)
    
    used = set()
    visited = []
    def test(cur, path):
        nonlocal visited, used
        # print(cur, path, used)
        if len(used) == len(tickets):
            # print("success")
            if len(visited) == 0:
                # print("changed")
                visited = path.copy();
            return;
        
        for (key, next) in fromto[cur]:
            if key in used:
                continue
            used.add(key)
            path.append(next)
            # print(key, cur, next, path)
            test(next, path)
            path.pop()
            used.remove(key)
    
    test("ICN", ["ICN"])
    return visited