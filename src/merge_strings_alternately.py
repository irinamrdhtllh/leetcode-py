def mergeAlternately(word1: str, word2: str) -> str:
    out = ""
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            out += word1[i]
        if i < len(word2):
            out += word2[i]
    return out
