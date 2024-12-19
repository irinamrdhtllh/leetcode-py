from typing import List


def compress(chars: List[str]) -> int:
    s = []
    n = 0
    for i in range(len(chars)):
        if len(s) == 0:
            s.append(chars[i])
            n += 1
        elif chars[i] == s[-1]:
            n += 1
        elif chars[i] != s[-1]:
            if n > 1:
                s.extend(list(str(n)))
            s.append(chars[i])
            n = 1

        if i == len(chars) - 1 and n > 1:
            s.extend(list(str(n)))

    chars[:] = s

    return len(chars)
