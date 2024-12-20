def closeStrings(word1: str, word2: str) -> bool:
    ch_map1 = {}
    ch_map2 = {}

    for ch in word1:
        if ch in ch_map1.keys():
            ch_map1[ch] += 1
        else:
            ch_map1[ch] = 1

    for ch in word2:
        if ch in ch_map2.keys():
            ch_map2[ch] += 1
        else:
            ch_map2[ch] = 1

    keys = sorted(list(ch_map1.keys())) == sorted(list(ch_map2.keys()))
    values = sorted(list(ch_map1.values())) == sorted(list(ch_map2.values()))

    return keys and values
