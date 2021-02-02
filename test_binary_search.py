import pytest

import run


@pytest.mark.parametrize("test_input, number, expected", [
    ([i for i in range(10)], 0, 0),
    ([i for i in range(10)], 9, 9),
    ([i for i in range(10)], -1, None),
    ([i for i in range(10)], 10, None),
    ([i for i in range(-10, 10)], -10, 0),
    ([i for i in range(-10, 10)], 9, 19),
    ([i for i in range(-10, 0)], -10, 0),
    ([i for i in range(-10, 0)], -1, 9),
])
def test_binary_search_1d(test_input, number, expected):
    assert run.binary_search_1d(test_input, number) == expected


@pytest.mark.parametrize("test_input, number, expected", [
    ([[i+(j*10) for i in range(10)] for j in range(10)], 0, (0, 0)),
])
def test_binary_search_2d(test_input, number, expected):
    assert run.binary_search_2d(test_input, number) == expected
