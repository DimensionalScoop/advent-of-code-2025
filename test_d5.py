import pytest
import d5


def check_db():
    db = d5.FreshnessDB([(1, 2), (4, 6), (5, 17)])
    assert db.min() == 1
    assert db.max() == 17
    assert db.is_fresh(10)
    assert db.is_fresh(1)
    assert db.is_fresh(17)
    assert not db.is_fresh(-1)
    assert not db.is_fresh(3)
    assert not db.is_fresh(18)


@pytest.fixture
def example_output():
    return (5, 11, 17)


@pytest.fixture
def example_input():
    return """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_extended(example_input, example_output):
    fresh_ranges, available = d5.parse_ingredients(example_input.split("\n"))
    db = d5.FreshnessDB(fresh_ranges)
    fresh_ingreditens = [i for i in available if db.is_fresh(i)]
    assert tuple(fresh_ingreditens) == example_output


# def test_parse():
#     lines = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32\n"
#     fresh, avail = parse_ingredients(lines)
