import pytest
from tinystats import mean, median

@pytest.mark.parametrize("nums,expected", [
    ([1], 1.0),
    ([1, 3], 2.0),
    ([1, 2, 3, 4], 2.5),
    ([10, -10, 10, -10], 0.0),
    ((1.5, 2.5), 2.0),
])
def test_mean(nums, expected):
    assert mean(nums) == pytest.approx(expected)

@pytest.mark.parametrize("nums,expected", [
    ([1], 1.0),
    ([1, 3], 2.0),
    ([1, 2, 3], 2.0),
    ([7, 1, 5, 3], 4.0),  # unsorted input
])
def test_median(nums, expected):
    assert median(nums) == expected

@pytest.mark.parametrize("func", [mean, median])
def test_empty_raises(func):
    with pytest.raises(ValueError):
        func([])

@pytest.mark.parametrize("func", [mean, median])
def test_non_iterable(func):
    with pytest.raises(TypeError):
        func(3)