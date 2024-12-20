def decodeString(s: str) -> str:
    stack = []
    curr_s = ""
    curr_n = 0

    for ch in s:
        if ch.isdigit():
            curr_n = 10 * curr_n + int(ch)
        elif ch == "[":
            stack.append((curr_n, curr_s))
            curr_s = ""
            curr_n = 0
        elif ch == "]":
            prev_n, prev_s = stack.pop()
            curr_s = prev_s + curr_s * prev_n
        else:
            curr_s += ch

    return curr_s
