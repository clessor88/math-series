import pytest

FIBONACCI_TABLE = [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
]

LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4)
]

CUSTOM_TABLE = [
    (3, 2, 3, 5),
    (4, 4, 5, 14)
]

@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci_iter(n, result):
    from series import fibonacci_iter
    assert fibonacci_iter(n) == result


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci_rec(n, result):
    from series import fibonacci_rec
    assert fibonacci_rec(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_iter(n, result):
    from series import lucas_iter
    assert lucas_iter(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_rec(n, result):
    from series import lucas_rec
    assert lucas_rec(n) == result


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_sum_series1(n, result):
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, one, two, result', CUSTOM_TABLE)
def test_sum_series2(n, one, two, result):
    from series import sum_series
    assert sum_series(n, one, two) == result

