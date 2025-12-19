import numpy as np
from collections import defaultdict

from common import read_lines


def parse_ingredients(lines: list):
    """
    >>> lines = getfixture('d5_example')
    >>> parse_ingredients(lines)
    ([(3, 5), (10, 14), ...], [1,  5,  8, 11, 17, 32])
    """
    split = lines.index("")
    fresh, available = lines[:split], lines[split + 1 :]
    fresh = [range_.split("-") for range_ in fresh]
    assert len(fresh[0]) == 2, fresh[0]
    fresh = [(int(a), int(b)) for a, b in fresh]
    available = np.asarray(available, dtype="int").tolist()
    return fresh, available


class FreshnessDB:
    def __init__(self, fresh_ranges):
        # build an index
        fresh_ranges = sorted(fresh_ranges, key=lambda a: a[1])
        self.fresh_ranges = fresh_ranges
        self.fresh_ranges_sorted_by_start = sorted(fresh_ranges, key=lambda a: a[0])
        self.check_consistency()

    def check_consistency(self):
        for a, b in self.fresh_ranges:
            assert b >= a
            assert b <= self.max()
            assert a >= self.min(), f"\n{a} lower bound\n{self.min()}overall"

    def max(self):
        return self.fresh_ranges[-1][1]

    def min(self):
        return min([a for a, b in self.fresh_ranges])

    def is_fresh(self, i: int):
        for start, stop in self.fresh_ranges:
            if stop >= i >= start:
                return True
        return False

    def total_fresh_ingred(self):
        count = 0
        i = self.min()

        while i <= self.max():
            if self.is_fresh(i):
                stop = self._get_next_stop(i)
                count += stop - i + 1
                i = stop + 1
            else:
                try:
                    i = self._get_next_start(i)
                except LastIntervalException:
                    break

        return count

    def _get_next_stop(self, i):
        for start, stop in self.fresh_ranges:
            if stop >= i >= start:
                return stop
        raise ValueError(f"{i} is not fresh!")

    def _get_next_start(self, i):
        ranges = self.fresh_ranges_sorted_by_start
        for start, stop in ranges:
            if i < start:
                return start
        raise LastIntervalException()


class LastIntervalException(Exception):
    pass


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
    fresh_ranges, available = parse_ingredients(lines)
    db = FreshnessDB(fresh_ranges)
    assert db.is_fresh(db.max())
    fresh_ingreditens = [i for i in available if db.is_fresh(i)]
    print(len(fresh_ingreditens))

    print(db.total_fresh_ingred())
