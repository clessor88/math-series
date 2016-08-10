import pytest
import sys


def fibonacci_iter(n):
    """Return the nth value of the Fibonacci series using an iterative approach"""
    series = [0, 1]
    while len(series) < n:
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series[n - 1]


def fibonacci_rec(n, series=[0, 1]):
    """Return the nth value of the Fibonacci series using an recursive approach."""
    if n < len(series):
        return series[n - 1]
    else:
        series.append(series[-1] + series[-2])
        return fibonacci_rec(n, series)


def lucas_iter(n):
    """Return the nth value of the lucas series using an iterative approach."""
    series = [2, 1]
    while len(series) < n:
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series[n - 1]


def lucas_rec(n, series=[2, 1]):
    """Return the nth value of the lucas series using an recursive approach."""
    if n < len(series):
        return series[n - 1]
    else:
        series.append(series[-1] + series[-2])
        return fibonacci_rec(n, series)


def sum_series(n, one=0, two=1):
    """Return the nth value of a custom sum series."""
    series = [one, two]
    while len(series) < n:
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series[n - 1]


def main():
    if len(sys.argv) > 2:
        print(u'usage: ./series.py function (args)')
        sys.exit(1)
    else:
        print(u'This module defines functions that implement mathematical series.')

if __name__ == '__main__':
    main()