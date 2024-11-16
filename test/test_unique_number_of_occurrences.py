from unique_number_of_occurrences import uniqueOccurrences


def test_case_1():
    arr = [1, 2, 2, 1, 1, 3]
    actual = uniqueOccurrences(arr)
    expected = True
    assert actual == expected


def test_case_2():
    arr = [1, 2]
    actual = uniqueOccurrences(arr)
    expected = False
    assert actual == expected


def test_case_3():
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    actual = uniqueOccurrences(arr)
    expected = True
    assert actual == expected
