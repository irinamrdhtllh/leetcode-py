def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    i = len(str1)
    j = len(str2)
    while j:
        temp = i
        i = j
        j = temp % j
    return str1[:i]
