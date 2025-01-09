from src.keys_and_rooms import Solution


solution = Solution()


def test_case_1():
    rooms = [[1], [2], [3], []]
    actual = solution.canVisitAllRooms(rooms)
    expected = True
    assert actual == expected


def test_case_2():
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    actual = solution.canVisitAllRooms(rooms)
    expected = False
    assert actual == expected
