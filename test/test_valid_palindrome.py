from src.valid_palindrome import isPalindrome


def test_case_1():
    s = "A man, a plan, a canal: Panama"
    actual = isPalindrome(s)
    expected = True
    assert actual == expected

def test_case_2():
    s = "race a car"
    actual = isPalindrome(s)
    expected = False
    assert actual == expected

def test_case_3():
    s = " "
    actual = isPalindrome(s)
    expected = True
    assert actual == expected