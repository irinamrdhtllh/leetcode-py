from src.merge_strings_alternately import mergeAlternately


def test_case_1():
    word1 = "abc"
    word2 = "pqr"
    actual = mergeAlternately(word1, word2)
    expected = "apbqcr"
    assert actual == expected


def test_case_2():
    word1 = "ab"
    word2 = "pqrs"
    actual = mergeAlternately(word1, word2)
    expected = "apbqrs"
    assert actual == expected


def test_case_3():
    word1 = "abcd"
    word2 = "pq"
    actual = mergeAlternately(word1, word2)
    expected = "apbqcd"
    assert actual == expected
