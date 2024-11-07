def isValid(s: str) -> bool:
    pair_map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    stack = []
    for ch in s:
        if ch in pair_map.keys():
            stack.append(ch)
        else:
            if not stack or ch != pair_map[stack[-1]]:
                return False
            stack.pop()
    return not stack
