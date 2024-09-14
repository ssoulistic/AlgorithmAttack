def solution(user_id, banned_id):
    result_set = set()

    def check_regex(word):
        combo_set = set()
        for uid in user_id:
            matched = True
            if len(uid) == len(word):
                for i in range(len(word)):
                    if word[i] != "*":
                        if uid[i] != word[i]:
                            matched = False
                            break
            else:
                matched = False
            if matched:
                combo_set.add(uid)
        return combo_set

    pos = []
    for bid in banned_id:
        pos.append(list(check_regex(bid)))

    def backtrack(idx, selected):
        if len(selected) == len(banned_id):
            result_set.add(tuple(sorted(selected)))
            return
        if idx >= len(banned_id):
            return
        
        for uid in pos[idx]:
            if uid not in selected:
                selected.add(uid)
                backtrack(idx + 1, selected)
                selected.remove(uid)

    backtrack(0, set())
    return len(result_set)
