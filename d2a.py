import numpy as np


def get_input():
    file = "data/d2"
    with open(file, "r") as f:
        lines = f.readlines()

    ranges = lines[0].strip().split(",")
    return [block.split("-") for block in ranges]


def is_dub(number):
    """
    >>> is_dub(1111)
    True
    >>> is_dub(1213)
    False
    >>> is_dub(111)
    False
    >>> is_dub(123123)
    True
    """
    number = str(number)
    n = len(number)
    if n % 2 != 0:
        return False
    a, b = number[: n // 2], number[n // 2 :]
    return a == b


def get_dubs(start, stop, is_dub):
    """
    >>> get_dubs("11",22, is_dub)
    [11, 22]
    >>> get_dubs(38593856, "38593862", is_dub)
    [38593859]
    """
    start, stop = int(start), int(stop)
    interval = np.arange(start, stop + 1)
    dub_idx = [is_dub(number) for number in interval]
    return interval[dub_idx].tolist()


if __name__ == "__main__":
    all_dubs = [get_dubs(start, stop, is_dub) for start, stop in get_input()]
    print(sum([sum(l) for l in all_dubs]))
