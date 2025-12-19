import numpy as np
from collections import defaultdict

from common import read_lines


def parse_ingredients(lines: list):
    """
    >>> lines = getfixture('d5_example')
    >>> parse_ingredients(lines)
    ([(3, 5), (10, 14), ...], array([ 1,  5,  8, 11, 17, 32]))
    """
    split = lines.index("")
    fresh, available = lines[:split], lines[split + 1 :]
    fresh = [range_.split("-") for range_ in fresh]
    assert len(fresh[0]) == 2, fresh[0]
    fresh = [(int(a), int(b)) for a, b in fresh]
    available = np.asarray(available, dtype="int")
    return fresh, available


def create_fresh_db(fresh_ranges):
    """
    >>> db = create_fresh_db([(1,100), (50,110)])
    >>> db[1]
    True
    >>> db[110]
    True
    >>> db[111]
    False
    """
    db = defaultdict(lambda: False)
    for a, b in fresh_ranges:
        for i in range(a, b + 1):
            db[i] = True
    return db


if __name__ == "__main__":
    lines = read_lines("data/d5")
    print("parse")
    fresh_ranges, available = parse_ingredients(lines)
    print("create db")
    is_fresh = create_fresh_db(fresh_ranges)
    print("check freshness")
    fresh_ingreditens = [i for i in available if is_fresh[i]]
    print(len(fresh_ingreditens))
