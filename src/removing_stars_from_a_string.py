def removeStars(s: str) -> str:
    stack = []

    for ch in s:
        if ch == "*":
            if len(stack) > 0:
                stack.pop(-1)
        else:
            stack.append(ch)

    return "".join(stack)
