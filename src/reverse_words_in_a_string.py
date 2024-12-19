def reverseWords(s: str) -> str:
    s = s.split()
    new_s = []
    for i in range(len(s) - 1, -1, -1):
        if len(new_s) == 0:
            new_s.append(s[i])
        else:
            new_s.append(" ")
            new_s.append(s[i])
    new_s = "".join(new_s)
    return new_s
