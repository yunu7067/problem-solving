def solution(user_id, banned_id):
    ans = []
    for banid in banned_id:
        check_id = [id for id in user_id if len(banid) == len(id)]
        for (index, char) in enumerate(banid):
            check_id = [id for id in check_id if char == "*" or id[index] == char]
        ans.append(check_id)
        
    # print(ans)
    queue = [[0, set([id])] for id in ans[0]]
    allsets = []
    while queue:
        [cur_idx, ids] = queue.pop()
        if cur_idx == len(ans) - 1:
            if not any([not ids.difference(sets) for sets in allsets]):
                allsets.append(ids)
            continue
        for next_id in ans[cur_idx+1]:
            if next_id not in ids:
                next_ids = list(ids)
                next_ids.append(next_id)
                queue.append([cur_idx + 1, set(next_ids)])
    # print(allsets)
    
    return len(allsets)