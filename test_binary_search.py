import pytest

import run


@pytest.mark.parametrize("test_input, num, expected", [
    ([i for i in range(10)], 0, 0),
    ([i for i in range(10)], 9, 9),
    ([i for i in range(1)], 0, 0),
    ([i for i in range(2)], 0, 0),
    ([i for i in range(2)], 1, 1),
    ([i for i in range(3)], 0, 0),
    ([i for i in range(3)], 1, 1),
    ([i for i in range(3)], 2, 2),
    ([i for i in range(4)], 0, 0),
    ([i for i in range(4)], 1, 1),
    ([i for i in range(4)], 2, 2),
    ([i for i in range(4)], 3, 3),
    ([i for i in range(0, 10, 2)], 2, 1),
    ([i for i in range(0, 10, 2)], 8, 4),
    ([i for i in range(10)], 69, None),
    ([i for i in range(-10, -1)], -2, 8),
    ([i for i in range(-10, -1)], -20, None),
    ([i for i in range(-10, 0)], -1, 9),
    ([i for i in range(-10, 0)], 1, None),
    ([i for i in range(-10, 10)], 9, 19),
    ([i for i in range(-10, 10)], 90, None),
])
def test_binary_search(test_input, num, expected):
    assert run.binary_search(test_input, 0, len(test_input)-1, num) == expected
