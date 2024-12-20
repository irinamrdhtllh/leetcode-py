def maxVowels(s: str, k: int) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    i = 0
    j = k
    n = 0
    max_n = 0

    for ch in s[i:j]:
        if ch in vowels:
            n += 1
    max_n = n

    while j < len(s):
        if s[i] in vowels:
            n -= 1
        if s[j] in vowels:
            n += 1
        if n > max_n:
            max_n = n
        i += 1
        j += 1

    return max_n
