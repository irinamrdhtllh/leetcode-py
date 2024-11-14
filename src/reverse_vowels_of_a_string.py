def reverseVowels(s: str) -> str:
    s = list(s)
    vowels = set("AaEeIiOoUu")

    i = 0
    j = len(s) - 1
    while j > i:
        if s[i] in vowels and s[j] in vowels:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1

    s = "".join(s)

    return s
